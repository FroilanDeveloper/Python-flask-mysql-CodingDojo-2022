from flask_app import app
from flask import flash 
# Flash Messages
from flask import redirect, render_template, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
# import User class from model
bcrypt = Bcrypt(app)


@app.route("/")
def index():
  return render_template("loginandregistration.html")


@app.route('/register',methods=['POST'])
def register():
  if not User.validate_register(request.form):
    return redirect('/')
  data ={ 
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    "password": bcrypt.generate_password_hash(request.form['password'])
  }
  id = User.save(data)
  session['user_id'] = id
  return redirect('/loginsuccess')

@app.route('/login',methods=['POST'])
def login():
  user = User.get_by_email(request.form)

  if user == None:
    flash("Invalid Email","login")
    return redirect('/')
  if not bcrypt.check_password_hash(user.password, request.form['password']):
    flash("Invalid Password","login")
    return redirect('/')
  session['user_id'] = user.id
  return redirect('/loginsuccess')

@app.route('/loginsuccess')
def home_page():
  if 'user_id' not in session:
    return redirect('/logout')
  data ={
    'id': session['user_id']
  }
  return render_template("loginsuccess.html",user=User.get_by_id(data))

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')