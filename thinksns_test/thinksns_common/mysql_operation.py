import pymysql


def get_verfied_code(session):
    """
    function；获取验证码
    :param session:
    :return:
    """
    select_sql = "select code from ts_verifycode where session = '%s' ORDER BY id DESC limit 0,1" % session
    ver_code = excute_mysql(select_sql)[0][0]
    return ver_code


def excute_mysql(select_sql):

    # db = pymysql.connect(host="192.168.102.151",user= "root", passwd="123456",db= "thinksns_test")
    db =pymysql.connect(host="192.168.102.151",user= "root", db= "thinksns_test")
    # 创建游标
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(select_sql)
    data = cursor.fetchall()
    return data
