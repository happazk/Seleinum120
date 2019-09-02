# 提供于数据库相关的操作方法
import pymysql

def get_verifycode(session):
    # 定义SQL语句
    sql = "SELECT code FROM ts_verifycode WHERE session='"+session+"' ORDER BY id DESC LIMIT 0,1;"
    # 调用执行方法
    verifycode = execute_sql(sql)[0][0]
    # 返回验证码
    return verifycode    

def execute_sql(sql):
    # 连接数据库，参数说明：IP和端口（默认3306，可不写），账号，密码，库名
    db = pymysql.connect("172.31.31.100", "thinksns_test", "123456","thinksns_test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()方法执行 SQL 查询   
    cursor.execute(sql)
    # 使用 fetchall() 方法获取所有数据
    data = cursor.fetchall()
#     print(data)
    # 关闭数据库连接
    db.close()
    # 返回数据内容
    return data

if __name__ == "__main__":
    print(get_verifycode("kkv4rbn2gsco49qfc0e4itmbn0"))
    
    