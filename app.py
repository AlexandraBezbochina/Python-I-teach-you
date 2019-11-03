from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def new_page():
    return 'Hello!'

@app.route('/<name>')
def page_with_name (name):
    return 'Имя: {}'.format(name)

from flask import render_template

@app.route('/check_age/<int:number>')
def check_age (number):
    return render_template('index1.html',title='Проверка возраста',age=number)

@app.route('/users')
def users_set():
    users=['Nick','Alex','Harry']
    return render_template('index2.html',title='Пользователи',users=users)

@app.route('/input',methods=['GET','POST'])
def input_names():
    if request.method =='POST':
        username=request.form.get('username')
        return render_template('print.html', method=request.method, name=username.split(','))
    elif request.method =='GET':
        username = request.args.get('username')
        if username == None:
            return render_template('input.html')
        else:
            return render_template('print.html',method=request.method, name=username.split(','))
    return render_template('input.html')


if __name__=="__main__":
    app.run(debug=True)