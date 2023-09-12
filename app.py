from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def form():
  if request.method == "GET":
    with app.app_context():
      return render_template("calc.jinja")
  
  elif request.method == "POST":
    first_name = request.form["fname"]
    first_name_letters = list(first_name)
    sum = 0
    
    for letter in first_name_letters:
      sum += ord(letter)
    
    last_name = request.form["lname"]
    last_name_letters = list(last_name)

    for letter in last_name_letters:
      sum += ord(letter)
    return sum

@app.route("/display_sum")
def display_sum():
  with app.app_context():
      return render_template("display_sum.jinja")