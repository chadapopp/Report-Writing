from flask import session, redirect, url_for, request, render_template
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')