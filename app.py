from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret key"


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        with app.app_context():
            return render_template("calc.jinja")

    elif request.method == "POST":
        number1 = request.form.get("num1")

        try:
            number1 = float(number1)
        except:
            flash("Invalid input")
            return render_template("calc.jinja")

        number2 = request.form.get("num2")
        try:
            number2 = float(number2)
        except:
            flash("Invalid input")
            return render_template("calc.jinja")

        operation = request.form.get("operation")

        try:
            if operation == "add":
                result = number1 + number2
                operation = "+"
            elif operation == "subtract":
                result = number1 - number2
                operation = "-"
            elif operation == "multiply":
                result = number1 * number2
                operation = "*"
            else:
                result = number1 / number2
                operation = "/"
        except:
            flash("Math error: cannot divide by zero")
            return render_template("calc.jinja")

        return render_template(
            "calc.jinja",
            result=result,
            number1=number1,
            number2=number2,
            operation=operation,
        )


if __name__ == "__main__":
    app.run()
