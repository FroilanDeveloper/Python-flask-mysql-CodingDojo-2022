from flask import render_template, redirect, request

from flask_app import app

from flask_app.controllers.users import User

@app.route('/')
def index():
  return redirect('/show_users')

@app.route('/user/create', methods=['POST'])
def create():
  print(request.form)
  User.save(request.form)
  return redirect('/show_users')


@app.route('/user/update',methods=['POST'])
def update():
  User.update(request.form)
  return redirect('/show_users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
  data ={
    'id': id
    } 
  User.destroy(data)
  return redirect('/show_users')

@app.route('/show_users')
def users():
  users=User.get_all()
  return render_template("show_users.html", users=users)

@app.route('/user/new')
def new():
  return render_template("new_users.html")


@app.route('/user/edit/<int:id>')
def edit(id):
  data ={ 
    "id":id
  }
  User.get_one(data)
  return render_template("edit_user.html")

@app.route('/user/1/<int:id>')
def show(id):
  data ={ 
    "id":id
    }
  User.get_one(data)
  return render_template("1_user.html")