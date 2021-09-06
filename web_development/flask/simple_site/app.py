from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


#create an instance of a flask application
app = Flask(__name__)
app.secret_key = "mikimiki"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime =  timedelta(days=5)

db = SQLAlchemy(app)



@app.route("/")
def home():
	return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True #set the duration you would like this session to last
		user =  request.form["nm"]
		session["user"] = user
		flash("login Succesful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]

		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
 			return render_template("user.html", email="email")
	else:
		flash("You are not logged in!")
		return redirect("login.html")

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You have been logged out {user}", "info")
	session.pop("user", None)
	return redirect(url_for("login"))
'''
#the concept of redirecting
@app.route("/<name>")
def user(name):
	return f"Hello {name}"

@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin!"))
'''

#run the app application
if __name__ == "__main__":
	app.run(debug=True)