import socket  # 导入 socket 模块
import time
from threading import Thread
from queue import Queue,LifoQueue,PriorityQueue
import json
import pymysql
'''
/*
 * ***************************************************************************************
 * @brief 钢丝绳远程智能监控系统服务端程序，需配合现场端软件与服务端软件使用
 * @file server.py
 * @author 张宏伟
 * @E-mail:bazhangya@hotmail.com
 * @QQ:515615456
 * @version V1.0
 * @data 2021-11-15
 * **************************************
 * @attention
 * 
 * 运行平台：linux服务器，阿里云的ubuntu实测可行
 * 运行环境：python3
 * 指令集：send,baseName get,baseName get,navtable
 * @log
 * 2021-11-15添加了注释
 * 2021-11-16添加了g_navTable字典，删除了之前的先进先出队列，解决了无数据时无限等待的问题
 * 2021-11-18 新指令，get,navtable
 * 2021-11-19 
 * 2021-11-27 新指令，getDamage,all
 * 2022-3-21 指令总结如下：
 *                      get,navtable：获取当前的所有设备，在线的，离线的，损伤数，地址 
 * ****************************************************************************************
**/
'''
host = socket.gethostname()# 获取本地主机名
g_ADDRESS = (host, 8889)  # 绑定地址
g_socket_server = None  # 负责监听的socket
g_conn_pool = []  # 连接池，主要用于获取当前在线的socket，但是不准
g_navTable = {} #全局导航字典 "name"->"data"
g_damageStats = {
}#全局损伤统计字典 "baseNme"->"number"
'''
/*
 * @brief 初始化服务器socket函数
 * @param 无
 * @retval 无
*/
'''
def init():#主函数首先调用
    '''
    初始化服务端SOCKET
    '''
    global g_socket_server
    global g_ADDRESS
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
    g_socket_server.bind(g_ADDRESS)
    g_socket_server.listen(10)  # 最大等待数（有很多人理解为最大连接数，其实是错误的）
    print("服务端已启动，等待客户端连接...")
'''
/*
 * @brief 服务器socket循环接受新来的socket连接
 * @param 无
 * @retval 无
*/
'''
def accept_client():#子线程循环执行这个
    '''
    接收新连接
    '''
    while True:
        client , adress = g_socket_server.accept()  # 阻塞，等待客户端连接
        # 加入连接池
        g_conn_pool.append(client)
        # 给每个客户端创建一个独立的线程进行管理
        thread = Thread(target=message_handle, args=(client,))
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()
        print("一个用户上线了.......")
'''
/*
 * @brief 服务器socket接受新socket连接后,处理消息，主要包括：判断模式，循环处理直至断开连接
 * @param client
 * @retval 无
*/
'''
def message_handle(client):
    '''
    消息处理
    '''
    print("等待客户端消息")
    #client.sendall("连接服务器成功!".encode(encoding='utf8'))
    while True:
        bytess = client.recv(1280)
        print("客户端消息:", bytess.decode(encoding='utf8'))
        bytesStr = str(bytess,encoding = "utf-8")
        '''
        * handle message "get,navtable"
        '''
        if bytesStr == "get,navtable":
            sendStr = count_navTable()
            print(sendStr)
            data = json.dumps(sendStr)
            client.sendall(bytes(data.encode('utf-8')))
        '''
        * handle message "getDamage,all" ps:这个指令已经被废弃,get,navtable包括其所有的功能
        '''
        if bytesStr == "getDamage,all":
            if g_damageStats == {}:
                client.sendall("null".encode())
                client.close()
            else:
                retStr = ''
                for k,v in dic.items():
                    retStr = retStr + k + "," + str(v) + ","
                client.sendall(retStr.encode())
                client.close()
        '''
        * 切分,分割的指令
        '''        
        progMode,baseName = bytesStr.split(",")
        '''
        * handle message "send,baseName"
        '''
        if progMode =="send":
            print("客户端消息上传模式")
            client.send('GetDamageData'.encode('utf-8'))
            client_send_handle_func(client,"send",baseName)
            g_conn_pool.remove(client)
            print("有一个客户端下线了。")
            break
        '''
        * handle message "get,baseName"
        '''
        if progMode =="get":
            print("客户端下载模式")
            client_get_handle_func(client,"get",baseName)
            g_conn_pool.remove(client)
            print("有一个客户端下线了。")
            break
        '''
        * handle message "sendDamage,baseName.<damageNum>"
        '''
        if progMode =="sendDamage":
            print("客户端上传损伤")
            realBaseName,strSecond = baseName.split(".")
            if realBaseName in g_damageStats.keys():
                g_damageStats[realBaseName] = g_damageStats[realBaseName]+1
            else:
                g_damageStats[realBaseName] = 1
            break
        if len(bytess) == 0:
            client.close()
            # 删除连接
            g_conn_pool.remove(client)
            print("有一个客户端下线了。")
            break
'''
/*
 * @brief 发送"send"数据模式
 * @param client send_flag baseName
 * @retval 无
*/
'''
def client_send_handle_func(client,send_flag,baseName):#先发send进入此模式
    if send_flag == "send":
        g_navTable[baseName] = Queue(maxsize=40)
        while True:
            time.sleep(0.002)#很重要不要删，时间匹配防止出现粘包问题
            try:
                bytess = client.recv(1280)
                bytessLen = len(bytess) 
                print(bytessLen)
            except:
                print("--------------------------")
                print("消息接收失败")
                print("--------------------------")
                client.close()
                g_navTable.pop(baseName)#删除字典
                print("发送模数客户端下线了。")
                client.close()
                break
            if bytessLen == 0:
                client.close()
                g_navTable.pop(baseName)#删除字典
                print("发送模式客户端下线了。")
                break
            elif g_navTable[baseName].full():
                _ = g_navTable[baseName].get()
            if bytessLen < 1280:
                try:
                    bytesStr = str(bytess,encoding = "utf-8")
                    progMode,strSecond = bytesStr.split(",")
                    if progMode =="sendDamage":
                        print("客户端上传损伤")
                        baseName,damageNum = strSecond.split(".")
                        if baseName in g_damageStats.keys():
                            insertEquipment(baseName,'武汉',g_damageStats[baseName][2]+int(damageNum),0)
                            g_damageStats[baseName][2] = g_damageStats[baseName][2]+int(damageNum)
                        else:
                            insertEquipment(baseName,'武汉',int(damageNum),0)
                            count_navTable()
                except:
                    pass
            elif bytessLen >= 1280:
                g_navTable[baseName].put(bytess)
'''
/*
 * @brief 获取"get"数据模式，循环处理
 * @param client send_flag baseName
 * @retval 无
*/
'''
def client_get_handle_func(client,get_flag,baseName):#先发get进入此模式
    if get_flag == "get":
        if baseName in g_navTable.keys():
            client.sendall("baseIsExis".encode())
        else:
            client.sendall("baseIsNotExis".encode())
            client.close()
            return
        while True:
            time.sleep(0.01)#很重要不要删，时间匹配防止出现粘包问题
            try:
                bytess = client.recv(1280)
                bytessLen = len(bytess)
            except:
                print("--------------------------")
                print("消息接收失败")
                print("--------------------------")
                client.close()
                break
            if bytessLen == 0:
                client.close()
                break
            try:
                bytesStr = str(bytess,encoding = "utf-8")
                progMode,baseName = bytesStr.split(",")
            except:
                pass
            if progMode =="get":
                if baseName not in g_navTable:
                    pass
                    #client.sendall("empty".encode())
                elif g_navTable[baseName].empty() == False:
                    try:
                        client.sendall(g_navTable[baseName].get())
                    except:
                        print("--------------------------")
                        print("消息发送失败")
                        print("--------------------------")
                        client.close()
                        break
                else:
                    try:
                        pass
                        #client.sendall("empty".encode())
                    except:
                        print("--------------------------")
                        print("消息发送失败")
                        print("--------------------------")
                        client.close()
                        break
'''
/*
 * @brief 查询所有在线的监测点
 * @param 无
 * @retval 字符串，以","分割的地点汇总
*/
'''
def count_navTable():
    server_Ip = "118.178.187.119"
    sql_Port = 3306
    sql_Username = "cnc_monitor"
    sql_Password = "123456"
    sql_Database = "cnc_monitor"
    table_name = "baseInfo"
    try:
        # 打开数据库连接
        conn = pymysql.connect(host=server_Ip, port=sql_Port, user=sql_Username, passwd=sql_Password, database=sql_Database, charset='utf8')
        cursor = conn.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM baseInfo"
        # 执行SQL语句
        cursor.execute(sql)
        #print(cursor.rownumber)
        result = cursor.fetchone()
        while result!=None:
            equipmentRes = list(result)
            g_damageStats[equipmentRes[0]] = equipmentRes
            result = cursor.fetchone()
        print(g_damageStats)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        pass
    return g_damageStats
'''the end of count_navTable'''

'''
/*
 * @brief 向数据库写入新设备或者更新设备数据
 * @param 无name,base,damageNum,onLineState
 * @retval 无
*/
'''
def insertEquipment(name,base,damageNum,onLineState):
    server_Ip = "118.178.187.119"
    sql_Port = 3306
    sql_Username = "cnc_monitor"
    sql_Password = "123456"
    sql_Database = "cnc_monitor"
    table_name = "baseInfo"    
    conn = pymysql.connect(host=server_Ip, port=sql_Port, user=sql_Username, passwd=sql_Password, database=sql_Database, charset='utf8')
    cursor = conn.cursor()
    mysql_sql = "INSERT INTO {}({}) VALUE ('{}','{}',{},{});".format(table_name,"name,base,damageNum,onLineState",name,base,str(damageNum),str(onLineState))
    try:
        cursor.execute(mysql_sql)
    except:
        mysql_sql = "update baseInfo set base = '{}',damageNum = {},onLineState = {} where name = '{}';".format(base,str(damageNum),str(onLineState),name)
        print(mysql_sql)
        cursor.execute(mysql_sql)
'''the end of insertEquipment'''

if __name__ == '__main__':
    init()
    # 新开一个线程，用于接收新连接
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    # 主线程逻辑
    while True:
        cmd = input("""--------------------------
输入1:查看当前在线用户数量
输入2:给指定客户端发送消息
输入3:关闭服务端
""")
        if cmd == '1':
            print("--------------------------")
            print("当前在线用户数量：", len(g_conn_pool))
            print("--------------------------")
        elif cmd == '2':
            print("--------------------------")
            index, msg = input("请输入“索引,消息”的形式：").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding='utf8'))
        elif cmd == '3':
            print("--------------------------")
            print("bye")
            print("--------------------------")
            exit()
        elif len(cmd) > 0:
            print("--------------------------")
            print("无法识别的指令")
            print("--------------------------")
'''the end of main'''

