from flask import Flask,render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__,template_folder="template")



@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == '+'):
        result = var_1 + var_2
    elif(operation == '-'):
        result = var_1 - var_2
    elif(operation == '*'):
        result = var_1 * var_2
    elif(operation == '/'):
    return render_template('resultado.html', entry=entry)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)