from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from micro.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=10, max=100)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign Up')
	
	def validate_email(self, email):
	 	user = User.query.filter_by(email=email.data).first()
	 	if user:
	 		raise ValidationError('This email is taken, please choose another one')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')
	
	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('This email is taken, please choose another one')

class MicroserviceForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	kategories = 
	stek = db.Column(db.String(20), nullable=False)
	get_apps = db.Column(db.String(100))
	request_apps = db.Column(db.String(100))
	link = StringField('Link', validators=[DataRequired()])
	submit = SubmitField('Post')
