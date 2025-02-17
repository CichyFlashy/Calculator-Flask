from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=["POST", "GET"])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html')
    else:
        return render_template('calculator_result.html')


if __name__ == "__main__":
    app.run()