from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


if __name__ == "__main__":
    app.run()