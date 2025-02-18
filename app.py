from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.debug = True

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=["POST", "GET"])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html')
    else:
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        operation = request.form['operation']
        return render_template('calculator_result.html', result=calculate(number1, number2, operation))


if __name__ == "__main__":
    app.run(debug=True)