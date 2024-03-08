from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def weather_report(station, date):
    # df = pandas.read_csv("weather.csv")
    temperature = 25
    result = {
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return result

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)