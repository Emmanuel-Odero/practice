'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisshouldbesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./site.db'
db = SQLAlchemy(app)

class Members(db.Model):
	my_link = db.Column(db.String(20), primary_key=True)
	username = db.Column(db.String(20), unique=True)
	joining_link = db.Column(db.String(20), unique=False)

if __name__ == '__main__':
	app.run(debug=True)'''
