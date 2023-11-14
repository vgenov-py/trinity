from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def t_home():
    return render_template("index.html")
