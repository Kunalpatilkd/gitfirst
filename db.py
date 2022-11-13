import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="study",port=3306)


def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into author values (%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()


def bloginsert(v):
    con=connect()
    cur=con.cursor()
    sql="insert into authorpost values (%s,%s,%s)"
    cur.execute(sql,v)
    con.commit()
    con.close()


def Authorcheck(email):
    con=connect()
    cur=con.cursor()
    sql="select Email_id,Password from author where Email_id=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data    


def selectAllpost():
    con=connect()
    cur=con.cursor()
    sql="select * from authorpost"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data



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






       




