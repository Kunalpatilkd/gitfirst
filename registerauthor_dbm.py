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
    sql="select Email_id,Password from Author where Email_id=%s"
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


def editdetails(e):
    con=connect()
    cur=con.cursor()
    sql="select * from author where email=%s"
    cur.execute(sql,e)
    userdetails=cur.fetchall()
    con.commit()
    con.close()
    return userdetails


def update(t):
    con=connect()
    cur=con.cursor()
    sql="update author set name=%s,city=%s,email=%s,pasword=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()


def drop(e):
    con=connect()
    cur=con.cursor()
    sql="delete from author where email=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()
    
