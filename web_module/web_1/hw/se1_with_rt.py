from flask import Flask, render_template
from decimal import Decimal
from math import ceil

app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def cal_bmi(weight, height):
    bmi_decimal = Decimal(weight) / (Decimal(height) ** Decimal(height))
    bmi = ceil(bmi_decimal * 100) / 100.0
    return render_template('bmi.html', bmi = bmi)

if __name__ == '__main__':
  app.run(debug=True)
