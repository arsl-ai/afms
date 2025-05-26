from flask import Flask, render_template
from jinja2 import Environment

app = Flask(__name__)


@app.route("/")
@app.route("/my_cars")
def index():
	return render_template("my_cars.html")


@app.route("/add_car")
def add_car():
	return render_template("add_car.html")


@app.route("/track_cars")
def track_cars():
	return render_template("track_my_cars.html")

if __name__ == '__main__':
	app.run(debug=True)