from flask import Flask
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "whateveryou123213432"

# Define the folder for uploaded files
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create the upload directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
