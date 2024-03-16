from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        data = {
            "full_name": full_name,
            "email": email
        }
        return render_template("confirmation.html",data)
    
    elif request.method == "GET":
        return render_template("index.html")

app.run(debug=True, port=5000)