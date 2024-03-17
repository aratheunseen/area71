from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "hidden-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        date = request.form["available_date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["employment"]

        form = Form(full_name=full_name,email=email,date=date_obj,occupation=occupation)
        db.session.add(form)
        db.session.commit()

        flash("Your form was submitted successfully.", "success")

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)