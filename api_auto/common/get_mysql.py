import pymysql

def get_sql(sql):



    #建立连接对象host,user,password,database,port,charset
    db = pymysql.connect(host = '数据库ip' ,user='数据库名字')
    #建立一个游标
    cursor = db.cursor()
    #运行sql语句
    cursor.execute(sql)
    #把sql运行数据保存在data变量里
    data= cursor.fetchall()#获取查询出的所有的值
    #关闭游标
    cursor.close()
    #关闭数据库连接
    db.close()
    #返回查询数据
    return data