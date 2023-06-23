from flask import render_template, request, redirect

from flask_app import app   

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninja_form')
def show_form():
    all_dojos = Dojo.get_all()

    return render_template('ninja_form.html',all_dojos=all_dojos)



@app.route('/submit_ninja_form', methods=['POST'])
def submit_shinobi_form():

    data = {
        'dojo_id' : request.form['dojo_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }

    Ninja.add_ninja(data)
    
    return redirect(f"/dojo/{request.form['dojo_id']}")