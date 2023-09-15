from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FloatField, RadioField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = "secret key"

class CalcForm(FlaskForm):
    number1 = FloatField("Number One:", validators=[InputRequired()])
    number2 = FloatField("Number Two:", validators=[InputRequired()])
    operation = RadioField(choices=[("Add", "Add"), ("Subtract", "Subtract"), ("Multiply", "Multiply"), ("Divide", "Divide")])

@app.route("/", methods=["POST", "GET"])
def form():
    calc_form = CalcForm()
    if calc_form.validate_on_submit():
        if request.method == "GET":
         return render_template("calc.jinja", form=calc_form)

        else:
            number1 = calc_form.number1.data
            number2 = calc_form.number2.data
            operation = calc_form.operation.data
            
            try:
                if operation == "Add":
                    result = number1 + number2
                    operation = "+"
                elif operation == "Subtract":
                    result = number1 - number2
                    operation = "-"
                elif operation == "Multiply":
                    result = number1 * number2
                    operation = "*"
                else:
                    result = number1 / number2
                    operation = "/"
            except:
                flash("Math error: cannot divide by zero")
                return render_template("calc.jinja", form=calc_form)
       
            return render_template("calc.jinja", form=calc_form, result=result,  number1=number1,
            number2=number2,
            operation=operation)
    
    return render_template("calc.jinja", form=calc_form)


if __name__ == "__main__":
    app.run()
