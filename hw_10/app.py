# flask_web/app.py
from flask import Flask, render_template

app = Flask(__name__)

ARITHMETIC_FUNC = {'sum': '+', 'dif': '-', 'mult': '*', 'dev': '/'}


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello! It is flask calculator'


@app.route('/calc/<int:x>/<int:y>/<string:function>/', methods=['POST', 'GET'])
def calc(x, y, function):
    func = ARITHMETIC_FUNC.get(function)
    if func:
        try:
            return render_template('calc.html', x=x, y=y, function=str(func), result=eval(f'{x} {func} {y}'))
        except ZeroDivisionError:
            return render_template('zero_division_error.html')
    return render_template('incorrect_action.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

