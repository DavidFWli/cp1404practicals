from flask import Flask, request

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    try:
        celsius_value = float(celsius)
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        return f"{celsius} degrees Celsius is equal to {fahrenheit_value:.2f} degrees Fahrenheit."
    except ValueError:
        return "Invalid input. Please enter a valid number for Celsius temperature."

if __name__ == '__main__':
    app.run()
