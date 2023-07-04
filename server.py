from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key="Python is for Winners"

@app.route('/')
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    return render_template("index.html")

@app.route('/numbers', methods=['POST'])
def guess_number():
    session['numbers'] = int(request.form['numbers'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

