from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from libsite import db, bcrypt
from libsite.models import User
from libsite.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from libsite.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("books.books_list"))

	form =  RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f"Your account has been created, you can now log in!", 'success')
		return redirect(url_for("users.login"))
	return render_template('register.html', form=form)

@users.route("/")
@users.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("books.books_list"))

	form = LoginForm()
	if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				next_page = request.args.get('next')
				return redirect(next_page) if next_page else redirect(url_for('books.books_list'))
			else:
				flash("Login Unsuccessful. Please check email and password!", 'danger')
	return render_template('login.html', form=form)

@users.route("/logout")
def logout():
	logout_user()
	flash(f"You have been loged out", 'success')
	return redirect(url_for('users.login'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash(f"Your account has been updated", "success")
		return redirect(url_for('users.account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template("account.html", title="account", image_file=image_file, form=form)




@users.route('/reset_password', methods=["GET", "POST"])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for("books.books_list"))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash(f"An email has been sent with instructions to reset your password", 'info')
		return redirect(url_for('users.login'))
	return render_template("reset_request.html", title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=["GET", "POST"])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('books.books_list.home'))
	user = User.verify_reset_token(token)
	if user is None:
		flash(f"That is an invalid or expired token", 'warning')
		return redirect(url_for("users.reset_request"))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash(f"Your account has been updated, you can now log in!", 'success')
		return redirect(url_for("users.login"))
	return render_template("reset_token.html", title='Reset Password', form=form)