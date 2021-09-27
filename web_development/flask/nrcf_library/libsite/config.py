import os

class Config:
	SECRET_KEY ="5a33a013cd986572879e22f4db9fc784"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.sqlite'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'michaelteddy009@gmail.com'  #obtaining sensitive data saved in the system enviroment variables
	MAIL_PASSWORD = 'to be known'