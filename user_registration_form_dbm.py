import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="study",port=3306)

def userinsert(u):
    con=connect()
    cur=con.cursor()
    sql="insert into user values(%s,%s,%s,%s)"
    cur.execute(sql,u)
    con.commit()
    con.close()

def usercheck(email):
    con=connect()
    cur=con.cursor()
    sql="select Email_id,Password from user where Email_id=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def showdata():
    con=connect()
    cur=con.cursor()
    sql="select * from user"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data