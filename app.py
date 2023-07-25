from flask import Flask, render_template, jsonify, request
import numpy as np
#Get is through URL and POST is through body.
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/postman_data', methods = ['POST'])
def MathOps():
    if (request.method == "POST"):
        ops = request.json['operation']
        n1 = int(request.json['num1'])
        n2 = int(request.json['num2'])

        if(ops == "add"):
            r = n1 + n2
            res = "The sum of " + str(n1) + " and " + str(n2) + " is " + str(r)
        if(ops == "multiply"):
            r = n1 * n2
            res = "The product of " + str(n1) + " and " + str(n2) + " is " + str(r)
        if(ops == "divide"):
            r = n1 / n2
            res = "The division of " + str(n1) + " and " + str(n2) + " is " + str(r)
        if(ops == "subtract"):
            r = n1 - n2
            res = "The subtraction of " + str(n1) + " and " + str(n2) + " is " + str(r)
        
        return render_template('results.html', result = res)


if __name__ == "__main__":
    app.run(debug = True)