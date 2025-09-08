# main.py ( opsional, gada guna, lengkapin aja, soalnya smua code ada di index.py )
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admission")
def admission():
    return render_template("admission.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

