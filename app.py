from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/')
def home():
	return render_template('index.html', posts=Post.select().order_by(Post.date.desc()))

@app.route('/new_post/')
def new_post():
	return render_template('add.html')

@app.route('/post/<int:post_id>')
def post(post_id):
	return render_template('post.html', post=Post.select().where(Post.id == post_id).get())

@app.route('/create/', methods=['POST'])
def create_post():
	Post.create(
		title=request.form['title'],
		subtitle=request.form['subtitle'],
		author=request.form['author'],
		text=request.form['text']
	)

	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True,port=8000)
