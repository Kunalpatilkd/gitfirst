from flask import *
from db import *


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registerauthor")
def regauthor():
    return render_template("registerauthor.html")
    
@app.route("/Userregistrationform")
def reguser():
    return render_template("Userregistrationform.html")

@app.route("/Login As Author")
def loginauthor():
    return render_template("Login As Author.html")

@app.route("/Login As User")
def loginuser():
    return render_template("Login As User.html")

@app.route("/Author Interface")
def Authorinterface():
    return render_template("Author Interface.html")

@app.route("/Add new blog post")
def Addnewblogpost():
    return render_template("Add new blog post.html")

@app.route("/Your Post")
def Yourposta():
    d=selectAllpost()
    return render_template("Your Post.html",data=d)
 


@app.route("/insertdata",methods=["post"])
def insertdata():
    Username=request.form["Username"]
    Password=request.form["password"]
    Email_id=request.form["Emailid"]
    City=request.form["City"]
    t=(Username,Password,Email_id,City)
    insert(t)
    return redirect("/")


@app.route("/userinsertdata",methods=["post"])
def userinsertdata():
    Username=request.form["Username"]
    Password=request.form["password"]
    Email_id=request.form["Emailid"]
    City=request.form["City"]
    u=(Username,Password,Email_id,City)
    userinsert(u)
    return redirect("/")


@app.route("/insertdata3",methods=["post"])
def newblogtdata():
    Authorname=request.form["author"]
    Blogtitle=request.form["blog title"]
    Blog=request.form["blog"]
    v=(Authorname,Blogtitle,Blog)
    bloginsert(v)
    return redirect("/")    

@app.route("/show_data",methods=["post"])
def shw():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=Authorcheck(email)
    if t in t1:
         return render_template("Author Interface.html")
    else:
  
        return render_template("home.html")

        

@app.route("/show_data1", methods=["post"])
def shw1():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=usercheck(email)
    if t in t1:
         return render_template("Your Post.html")
    else:
        
        return render_template("home.html")        







if __name__=='__main__':
    app.run(debug=True)


