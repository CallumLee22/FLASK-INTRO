from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        with app.app_context():
            return render_template("calc.jinja")

    elif request.method == "POST":
        number1 = request.form.get("num1")
        number3 = os.environ.get("NUMBER3")
        number3 = int(number3)

        try:
            number1 = int(number1)
        except:
            return "Input was not a number"

        num2 = request.form.get("num2")
        try:
            num2 = int(num2)
        except:
            return "Input was not a number"

        sum = number1 + num2 + number3
        return json.dumps(
            {"result": sum, "number1": number1, "number2": num2, "number3": number3},
            indent=4,
        )


@app.route("/display_sum")
def display_sum():
    with app.app_context():
        return render_template("display_sum.jinja")


app.run()
