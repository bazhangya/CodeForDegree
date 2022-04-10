import socket
import pymysql
import time
import json
import numpy as np
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cbook as cbook
import pandas as pd
from scipy.fftpack import fft,ifft
import seaborn

g_navTable = {}
def Axes3DPlot():
    #定义坐标轴
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    #ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图
    z = np.linspace(0,13,1000)
    x = 5*np.sin(z)
    y = 5*np.cos(z)
    zd = 13*np.random.random(100)
    xd = 5*np.sin(zd)
    yd = 5*np.cos(zd)
    ax1.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图
    ax1.plot3D(x,y,z,'gray')    #绘制空间曲线
    plt.show()
def myFFT():
    filepath = 'F:\\备份\\D盘\\高速试验台数据\\5hz.csv'
    msft = pd.read_csv(filepath)
    first_column_data = msft[msft.keys()[0]]
    second_column_data = msft[msft.keys()[1]]
    x = numpy.arange(0, len(first_column_data)/20000, 1/20000)
    y = list(first_column_data)
    fre_x,fft_y=FFT(20000,y)                     #快速傅里叶变换
    plt.subplot(221)
    plt.plot(x,y)   
    plt.title('Original wave')
    plt.subplot(222)
    plt.plot(fre_x,fft_y,'r')
    plt.title('FFT wave')

    plt.show()
'''the end of myFFT'''
def FFT (Fs,data):
    L = len (data)                        # 信号长度
    N =np.power(2,np.ceil(np.log2(L)))    # 下一个最近二次幂
    FFT_y1 = np.abs(fft(data,int(N)))/L*2      # N点FFT 变化,但处于信号长度
    Fre = np.arange(int(N/2))*Fs/N        # 频率坐标
    FFT_y1 = FFT_y1[range(int(N/2))]      # 取一半
    return Fre, FFT_y1
'''the end of FFT'''
def myPlot():
    #pltConfig()
    # numpy读取csv文件
    filepath = 'E:\\waterwell\\导入数据\\水气两相法导入数据\\生产数据1.csv'
    filepath = 'F:\\备份\\D盘\\5hz.csv'
    msft = pd.read_csv(filepath)
    first_column_data = msft[msft.keys()[0]]
    second_column_data = msft[msft.keys()[1]]
    x = numpy.arange(0, len(first_column_data)/20000, 1/20000)
    fig,ax=plt.subplots(1,1)
    ax.set_title('典型损伤信号',color='k')
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示
    plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
    #figsize(12.5, 4) # 设置 figsize
    #plt.rcParams['savefig.dpi'] = 300 #保存图片分辨率
    plt.rcParams['figure.dpi'] = 200 #分辨率
    # 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
    # 指定dpi=200，图片尺寸为 1200*800
    # 指定dpi=300，图片尺寸为 1800*1200
    plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
    #plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
    plt.savefig('plot1.png', dpi=300) #指定分辨率保存
    plt.xlabel('时间(s)')
    plt.ylabel('电压(1/4096)V')
    #设置坐标轴范围
    plt.xlim((0.3, 0.4))
    plt.ylim((1000, 3000))
    plt.plot(x,first_column_data,'r-',label='type1',linewidth=4)
    plt.show()
'''the end of myPlot'''
def watchSignal():
    filepath = 'F:\\备份\\D盘\\高速试验台数据\\5hz.csv'
    msft = pd.read_csv(filepath)
    first_column_data = msft[msft.keys()[0]]
    second_column_data = msft[msft.keys()[1]]
    third_column_data = msft[msft.keys()[2]]
    fourth_column_data = msft[msft.keys()[3]]
    x = numpy.arange(0, len(first_column_data)/20000, 1/20000)
    plt.subplot(411)
    plt.plot(x,list(first_column_data),'r-')   
    plt.title('signal 1')
    plt.subplot(412)
    plt.plot(x,list(second_column_data),'r-')
    plt.title('signal 2 ')
    plt.subplot(413)
    plt.plot(x,list(third_column_data),'r-')
    plt.title('signal 3')
    plt.subplot(414)
    plt.plot(x,list(fourth_column_data),'r-')
    plt.title('signal 4')

    plt.show()
'''the end of watch signal'''
def selectTest():
    server_Ip = "118.178.187.119"
    sql_Port = 3306
    sql_Username = "cnc_monitor"
    sql_Password = "123456"
    sql_Database = "cnc_monitor"
    table_name = "baseInfo"
    # 打开数据库连接
    conn = pymysql.connect(host=server_Ip, port=sql_Port, user=sql_Username, passwd=sql_Password, database=sql_Database, charset='utf8')
    cursor = conn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM baseInfo"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        #print(cursor.rownumber)
        result = cursor.fetchone()
        while result!=None:
            print(list(result), cursor.rownumber)
            result = cursor.fetchone()
    except:
        print ("Error: unable to fetch data")

    conn.commit()
    cursor.close()
    conn.close()

def insertTest(name,base,damageNum,onLineState):
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
        
    conn.commit()
    print(mysql_sql)
    cursor.close()
    conn.close()

def updateTest(name,base,damageNum,onLineState):
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
        mysql_sql = "update baseInfo set base = '{}',damageNum = damageNum+{},onLineState = {} where name = '{}';".format(base,str(damageNum),str(onLineState),name)
        print(mysql_sql)
        cursor.execute(mysql_sql)
        
    conn.commit()
    print(mysql_sql)
    cursor.close()
    conn.close()


def createTables():
    host = '118.178.187.119'
    port = 3306
    db = 'cnc_monitor'
    user = 'cnc_monitor'
    password = '123456'
    conn = pymysql.connect(host='118.178.187.119', port=3306, user=user, passwd=password, database='cnc_monitor',
                        charset='utf8')
    mysql_sql = 'CREATE TABLE baseInfo(name VARCHAR(16) unique key ,base VARCHAR(16),damageNum int,onLineState int);'
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS baseInfo")
    cursor.execute(mysql_sql)
    mysql_sql = 'INSERT INTO baseInfo(name,base,damageNum,onLineState) VALUE (%s,%s,%s,%s);'
    value = ('设备1','武汉',20,1)
    cursor.execute(mysql_sql, value)
    conn.commit()
    cursor.close()
    conn.close()

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
            g_navTable[equipmentRes[0]] = equipmentRes
            result = cursor.fetchone()
        print(g_navTable)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("sql error")
    return g_navTable

def jsonTest():
    ip = '118.178.187.119'
    port = 8889
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    dict = {'设备1': ['设备1', '武汉', 20, 1], '设备2': ['设备2', '南京', 20, 0], '设备3': ['设备3', '武汉', 2, 1], '设备4': ['设备4', '武汉', 2, 1], '设备5': ['设备5', '武汉', 2, 0]}
    print(dict['设备1'][2])
    data = json.dumps(dict)
    print(len(data))
    sock.send(bytes(data.encode('utf-8')))
    sock.close()
def dicTest():
    g_damageStats = {'设备1': ['设备1', '武汉', 20, 1], '设备2': ['设备2', '南京', 20, 0], '设备3': ['设备3', '武汉', 2, 1], '设备4': ['设备4', '武汉', 2, 1], '设备5': ['设备5', '武汉', 2, 0]}
    x=range(1,len(g_damageStats))
    y=[]
    labe=[]
    for key in g_damageStats:
        y.append(g_damageStats[key][2])
        labe.append(key)
    print(y)
    print(labe)
if __name__=='__main__':
    #createTables()
    #insertTest('设备4','武汉',5,0)
    #updateTest('设备6','武汉',2,0)
    #selectTest()
    #count_navTable()
    #dicTest()
    #jsonTest()
    #myPlot()
    #myFFT()
    #Axes3DPlot()
    watchSignal()
