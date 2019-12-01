from datetime import datetime
from micro import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False)
	role = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable=False)
	microservices_id = db.Column(db.Integer)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}'.'{self.image_file}')"
	

class Microservice(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	kategories = db.Column(db.String(20), nullable=False)
	stek = db.Column(db.String(20), nullable=False)
	get_apps = db.Column(db.String(100))
	request_apps = db.Column(db.String(100))
	user_id = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"
