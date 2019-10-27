from flask import Flask

app = Flask(__name__)

@app.route('/')
def new_page():
    return 'Hello!'

@app.route('/<name>')
def page_with_name(name):
    return 'Имя: {}'.format(name)

from flask import render_template

@app.route('/check_age/<int:number>')
def check_age(number):
    return render_template('index1.html',title='Проверка возраста',age=number)

@app.route('/users')
def users_set():
    users=['Nick','Alex','Harry']
    return render_template('index2.html',title='Пользователи',users=users)


if __name__=="__main__":
    app.run(debug=True)