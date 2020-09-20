import os

from flask import flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

from readingRacer import ALLOWED_EXTENSIONS, app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/speak/")
def select_grade_level():
    return render_template("speak.html")


@app.route("/reading-practice/")
def reading_practice():
    return render_template("readingpractice.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# taken from Flask documentation for uploading files
@app.route("/upload/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("get_uploaded", filename=filename))
    return render_template("upload.html")


# taken from Flask documentation for uploading files
@app.route("/uploads/<filename>")
def get_uploaded(filename):
    return send_file(os.path.join("static/client", filename))
