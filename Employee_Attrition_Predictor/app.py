from flask import Flask, render_template, request, url_for, redirect, session
import pickle
from sqlite3 import * 
from random import randrange
from flask_mail import Mail, Message

app=Flask(__name__)

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]="testertanay38@gmail.com"
app.config["MAIL_PASSWORD"]="qrlwyjzabsdmnhtn" 
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False

app.secret_key="Testertanayrocks"

mail=Mail(app)

@app.route("/fpassword", methods=["GET","POST"])
def fpassword():
	if request.method=="POST":
		em=request.form["em"]
		un=request.form["un"]
		con=None
		try:
			con=connect("user.db")
			cursor=con.cursor()
			sql="select password from users where username='%s'"
			cursor.execute(sql%(un))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("fpassword.html", msg="user doesn't exists")
			else:
				return render_template("fpassword.html", msg=data)

		except Exception as e:
			return render_template("fpassword.html", msg=e)
		finally:
			msg=Message("regarding forgotten password",sender="testertanay38@gmail.com",recipients=[em])
			msg.body="Your password is " + str(data) + "\n \n \nNote:\nIf there is a empty space in the place of password,then you are new user,please signup and create your account. \n \n Thank you!!!"				
			mail.send(msg)
			if con is not None:
				con.close()
			
	else:
		return render_template("fpassword.html")

@app.route("/logout",methods=["GET","POST"])
def logout():
	session.clear()
	return redirect (url_for("login"))


@app.route("/",methods=["GET","POST"])

def home():
	if "username" in session:
		return render_template("home.html",name=session["username"])
		
	else:
		return redirect(url_for("login"))

@app.route("/check")
def check():
	
	sl=float(request.args.get("sl"))
	
	le=float(request.args.get("le"))
	
	npr=int(request.args.get("npr"))
	
	amh=int(request.args.get("amh"))
	
	tsc=int(request.args.get("tsc"))

	wa=int(request.args.get("wa"))
	
	promo5=int(request.args.get("promo5"))
	
	dt=request.args.get("dt")
	if dt=='a':
		dept=0
	elif dt=='b':
		dept=1
	elif dt=='c':
		dept=2
	elif dt=='d':
		dept=3
	elif dt=='e':
		dept=4
	elif dt=='f':
		dept=5
	elif dt=='g':
		dept=6
	elif dt=='h':
		dept=7
	elif dt=='i':
		dept=8
	elif dt=='j':
		dept=9	

	sa=request.args.get("sa")
	if sa=='a':
		sal=0
	elif sa=='b':
		sal=1
	elif sa=='c':
		sal=2

	data=[[sl, le, npr, amh, tsc, wa, promo5, dept, sal]]

	with open("empl_attr.model", "rb") as f:
		model=pickle.load(f)			
	res=model.predict(data)
	return render_template("home.html",msg=res)

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method=="POST":
		un=request.form["un"]
		pw=request.form["pw"]
		con=None
		try:
			con=connect("user.db")
			cursor=con.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor.execute(sql%(un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("login.html",msg="invalid login")
			else:
				session["username"]=un
				session["password"]=pw
				return redirect(url_for("home"))
		except Exception as e:
			return render_template("login.html",msg=e)
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method=="POST":
		un=request.form["un"]
		pw1=request.form["pw1"]
		pw2=request.form["pw2"]
		if pw1==pw2:
			con=None
			try:
				con=connect("user.db")
				cursor=con.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql%(un,pw1))
				con.commit()
				return redirect(url_for("login"))
			except Exception as e:
				con.rollback()
				return render_template("signup.html",msg="user already exists")
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html",msg="password did not match")
	else:
		return render_template("signup.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)		