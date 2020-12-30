from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = "./readingRacer/static/client"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = '86pOqV7ltb6Wo-CEux6zPg'

import readingRacer.routes
