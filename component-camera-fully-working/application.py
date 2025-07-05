from flask import Flask, render_template
from flask import request
from requests import get

# Flask
app = Flask(__name__)



# ----- Main function 
@app.route('/output', methods = ['POST','GET'])
def main():
    return render_template('output.html')


# Default Home Route
@app.route('/')
def home():
    return render_template('camera_appear.html')


# ----- Calling the current file main function
if __name__ == "__main__":
    app.run(debug=True)
