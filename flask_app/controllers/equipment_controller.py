from flask import session, redirect, render_template, flash, request
from flask_app import app
from flask_app.models.equipment import Equipment
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/equipment/create_equipment', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        data = {
            "user_id": session["user_id"],
            "equipment_type": request.form["equipment_type"],
            "equipment_name": request.form["equipment_name"],
            "equipment_number": request.form["equipment_number"],
        }

        Equipment.equipment_save(data)
        return redirect('/user/dashboard')
    
    return render_template('/equipment/create_equipment.html')

@app.route('/equipment/edit_equipment/<int:equipment_id>', methods=['GET', 'POST'])
def edit_equipment(equipment_id):
    if request.method == 'POST':
        data = {
            "equipment_id": equipment_id,
            "equipment_type": request.form["equipment_type"],
            "equipment_name": request.form["equipment_name"],
            "equipment_number": request.form["equipment_number"],
        }

        Equipment.equipment_update(data)
        return redirect(f'/equipment/view_all_equipment/{session["user_id"]}')
    
    data = {"equipment_id": equipment_id}
    equipment = Equipment.get_one_equipment(data)
    return render_template('/equipment/edit_equipment.html', equipment=equipment)

@app.route('/equipment/view_all_equipment/<int:user_id>')
def get_all_equipment(user_id):
    data = {"user_id": user_id}
    equipment = Equipment.get_all_equipment_per_user(data)
    return render_template('/equipment/get_all_equipment.html', equipment=equipment)

# routes to get specific equipment per user

@app.route('/equipment/view_exchangers/<int:user_id>')
def get_exchangers(user_id):
    data = {"user_id": user_id}
    equipment = Equipment.get_all_exchangers_per_user(data)
    return render_template('/equipment/get_exchangers.html', equipment=equipment)

@app.route('/equipment/view_drums/<int:user_id>')
def get_drums(user_id):
    data = {"user_id": user_id}
    equipment = Equipment.get_all_drums_per_user(data)
    return render_template('/equipment/get_drums.html', equipment=equipment)

@app.route('/equipment/view_tower_reactor/<int:user_id>')
def get_tower_reactors(user_id):
    data = {"user_id": user_id}
    equipment = Equipment.get_all_towers_reactors_per_user(data)
    return render_template('/equipment/get_tower_reactor.html', equipment=equipment)

@app.route('/equipment/view_heaters/<int:user_id>')
def get_heaters(user_id):
    data = {"user_id": user_id}
    equipment = Equipment.get_all_heaters_per_user(data)
    return render_template('/equipment/get_heaters.html', equipment=equipment)

    