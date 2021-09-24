from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from libsite import db, login_manager
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)

	def get_reset_token(self, expires_sec=1800):  #for password reset funtionality
		s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Books(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(40), unique=False, nullable=False)
	age = db.Column(db.String(10), nullable=False)
	age_group = db.Column(db.String(10), nullable=False)
	copies = db.Column(db.Integer, nullable=False)
	category = db.Column(db.String(20), nullable=False)
	notes = db.Column(db.String(200), nullable=True)
	brought_by = db.Column(db.String(30), nullable=True)


	def __repr__(self):
		return f"Book('{self.title}', '{self.category}')"