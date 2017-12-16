from flask import Flask, render_template
from decimal import Decimal
from math import ceil

app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def cal_bmi(weight, height):
    bmi_decimal = Decimal(weight) / (Decimal(height) ** Decimal(height))
    bmi = ceil(bmi_decimal * 100) / 100
    if bmi < 16:
        result = 'severely underweight'
    elif bmi < 18.5:
        result = 'underweight'
    elif bmi < 25:
        result = 'normal'
    elif bmi < 30:
        result = 'overweight'
    else:
        result = 'obese'

    return '''<h1>BMI</h1>
            <h3>Your BMI is {0}</h3>
            <h4>You are {1}</h4>'''.format(bmi, result)

if __name__ == '__main__':
  app.run(debug=True)
