from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/calculate', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/caltulate', methods=['POST'])
def result():

    first = request.form['first']
    second = request.form['second']

    if not first.isdigit() or not second.isdigit():
        return 'Значения введены неверно: <a href="/calculate"> Назад </a>'

    first = int(first)
    second = int(second)
    operation = request.form['operation']
    res = 0


    if operation == 'add':
        res = first + second

    elif operation == 'sub':
        res = first - second

    elif operation == 'mul':
        res = first * second

    elif operation == 'div':
        if second == 0:
            return 'На ноль делить нельзя <a href="/calculate"> Назад </a>'
        res = first / second

    else:
        return 'Ошибка <a href="/calculate"> Назад </a>'

    return render_template('result.html', result=res)

if __name__ == '__main__':
    app.run(port=5001)