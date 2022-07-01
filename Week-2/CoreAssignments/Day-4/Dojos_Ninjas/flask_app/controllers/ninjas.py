from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
  dojos = Dojo.get_all()
  return render_template('ninjas.html', dojos=dojos)


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
  Ninja.save(request.form)
  return redirect('/')


@app.route('/dojo/<int:dojo_id>') #This will allow the app route to change when you click on dojo
def display_ninjas(dojo_id):
  data ={
    'dojo_id': dojo_id
  }
  print(dojo_id)
  ninjas = Ninja.get_one_with_ninjas(data)
  print(data)
  return render_template('dojo.html', ninjas=ninjas)

