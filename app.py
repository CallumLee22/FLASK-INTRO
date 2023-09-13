from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        with app.app_context():
            return render_template("calc.jinja")

    elif request.method == "POST":
        number1 = request.form.get("num1")

        try:
            number1 = int(number1)
        except:
            return "Input was not a number"

        number2 = request.form.get("num2")
        try:
            number2 = int(number2)
        except:
            return "Input was not a number"

        operation = request.form.get("operation")

        try:
            if operation == "add":
                result = number1 + number2
            elif operation == "subtract":
                result = number1 - number2
            elif operation == "multiply":
                result = number1 * number2
            else:
                result = number1 / number2
        except:
            result = 0

        return render_template("calc.jinja", result=result)


if __name__ == "__main__":
    app.run()
