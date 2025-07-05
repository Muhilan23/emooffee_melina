from flask import Flask, render_template
from _1_base64_to_img import img_convertion
from _3_emooffee_main import emooffee_analyse
from _4_content_levels import content_levels


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("_1_index.html")



@app.route("/picture.html")
def home():
	return render_template("_2_picture.html")



@app.route("/output.html")
def output():

	current_img_path = img_convertion("C:/Users/navee/Downloads/sample.txt")

	user_output = emooffee_analyse(current_img_path)

	content_levels(user_output)

	return render_template("_3_output.html")


@app.route("/_2_1_camera_appear.html")
def camera():
	return render_template("_2_1_camera_appear.html")


if __name__=="__main__":
	app.run(debug=True)
