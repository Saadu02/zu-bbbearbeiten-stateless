import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)
from flask import Response
from helper import get_csv
@app.route("/")
def index():
    items = helper.get_all()
    return render_template('index.html', items=items)


@app.route('/add', methods=["POST"])
def add():
    text = request.form.get("text")
    helper.add(text)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


@app.route("/download")
def download_csv():
    data = [
        {"title": "Meeting", "category": "Work", "description": "Weekly meeting"},
        {"title": "Shopping", "category": "Personal", "description": "Buy milk and bread"}
    ]
    return Response(
        get_csv(data),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=traktanden.csv"},
    )