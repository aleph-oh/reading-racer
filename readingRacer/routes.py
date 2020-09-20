import os
import getScore
from flask import flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

from readingRacer import ALLOWED_EXTENSIONS, app
from readingRacer.get_text import get_speech_recog


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/speak")
def speak():
    return render_template("speak.html")


@app.route("/watch")
def watch():
    return render_template("watch.html")


@app.route("/read")
def read():
    return render_template("read.html")


@app.route("/reading-practice/<int:grade>", methods=["GET", "POST"])
def reading_practice(grade):
    # if posted to: get next story from posted data, which should be prev. story and difficulty
    if request.method == "POST":
        # check if post request has file part
        try:
            file = request.files["file"]
        except KeyError:
            flash("Audio stream upload failed")
            return redirect(request.url)
        try:
            prev_text = request.values["previous"]
        except KeyError:
            flash("Failed to send previous text")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app["UPLOAD_FOLDER"], filename)
            # convert file to flac
            #file.save(path)
            # Pass file into api processing
            speech_recog = get_speech_recog(path)

            # determine accuracy of file
            (nextTitle, nextString, coloredString) = getScore.getScore(speech_recog, prev_text)
            # get new contents as colors

            # change links on page to reflect right / wrong-ness

    #story = get_story(grade)
    return render_template("reading_practice_init.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# taken from Flask documentation for uploading files
@app.route("/upload", methods=["GET", "POST"])
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
