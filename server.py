from flask import Flask, render_template, request # Import Flask, render_template, and request
from Maths.mathematics import summation, subtraction, multiplication # Import summation, subtraction, and multiplcation

app = Flask("Mathematics Problem Solver")

# Define app route for the summation function
@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return str(result)
    except ValueError:
        return "Please enter valid numeric values for both 'Number 1' and 'Number 2'."


# Define app route for the subtraction function
@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return str(result)
    except ValueError:
        return "Please enter valid numeric values for both 'Number 1' and 'Number 2'."


# Define app route for the multiplication function
@app.route("/mul")
def mul_route():
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))  
        result = multiplication(num1, num2)
        return str(result)
    except ValueError:
        return "Please enter valid numeric values for both 'Number 1' and 'Number 2'."

@app.route("/")
def render_index_page():
    return render_template('index.html')

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
