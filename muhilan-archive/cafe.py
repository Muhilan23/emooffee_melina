from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/picture.html")
def home():
	return render_template("picture.html")

@app.route("/output.html")
def output():
	return render_template("output.html")


if __name__=="__main__":
	app.run(debug=True)
