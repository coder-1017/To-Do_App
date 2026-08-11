from flask import render_template, redirect, url_for, request
from app import app
from app.models import Todo
from app import db

@app.route('/')
@app.route('/home')
def home():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    #request.form is a dictionary-like object in Flask that extracts 
    #data sent from an HTML form when a user submits it via an 
    #HTTP POST or PUT request.
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('home'))

# Specifying <int:id> automatically converts 'id' to an integer
@app.route('/complete/<int:id>')
def complete(id):
    # get_or_404 fetches by primary key or returns a 
    # 404 error page if not found
    todo = Todo.query.get_or_404(id)
    todo.complete = True
    db.session.commit()

    return redirect(url_for('home'))

