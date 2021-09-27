from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from libsite import db
from libsite.models import User, Books
from libsite.books.forms import BookForm


books = Blueprint('books', __name__)

@books.route("/books/list", methods=['GET', 'POST'])
@login_required
def books_list():
	return render_template("books.html")


@books.route("/books/new", methods=['GET', 'POST'])
@login_required
def new_book():
	form = BookForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash(f"New Book has been created!", 'success')
		return redirect(url_for('main.home'))
	return render_template("create_book.html", title="New Book", form=form, legend="New Book", page='create_book')