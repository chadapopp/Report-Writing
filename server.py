from flask_app import app
from flask_app.controllers import index_controller
from flask_app.controllers import user_controller
from flask_app.controllers import equipment_controller

if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True, port=5000)