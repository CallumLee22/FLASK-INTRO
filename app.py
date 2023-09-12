from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  with app.app_context():
        return render_template("calc.jinja")