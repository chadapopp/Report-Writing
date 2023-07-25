from flask import session, redirect, render_template, flash, request
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/user/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
            return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "api_number": request.form['api_number'],
        "password": pw_hash
    }
    User.save_user(data)
    return redirect('/user/dashboard')

@app.route('/user/login', methods=['POST'])
def login():
      user = User.get_by_email(request.form)
      if not user:
            flash("Invalid Email/Password", "login")
            return redirect('/')
      if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash("Invalid Email/Password", "login")
            return redirect('/')
      session['user_id'] = user.id
      return redirect('/user/dashboard')

@app.route('/user/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return 'you are not logged in, please login or register to continue'
    user = User.get_user_by_id(session['user_id'])
    print(user)
    return render_template('/user_pages/user_dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
