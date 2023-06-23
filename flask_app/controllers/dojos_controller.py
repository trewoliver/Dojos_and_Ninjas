from flask import render_template, request, redirect

from flask_app import app   

from flask_app.models.dojo_model import Dojo



@app.route('/')
def Home():
    all_dojos = Dojo.get_all()

    return render_template('index.html',all_dojos=all_dojos)


@app.route('/dojo/<int:id>')
def show_dojo_ninjas(id):

    return render_template('one_dojo.html', one_dojo_ninjas=Dojo.get_one( {'id' : id} ))


@app.route('/submit_dojo_form',methods=['POST'])
def Create_Dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')




