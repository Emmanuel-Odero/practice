from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	age = StringField('Age')
	age_group = StringField("Age Group")
	copies = StringField("Copies")
	category = StringField("Category")
	notes =StringField("Notes")
	brought_by = StringField("Brought By")
	submit = SubmitField("Add Book")