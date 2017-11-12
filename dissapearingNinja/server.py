from flask import Flask,redirect,request,session,flash,render_template

app = Flask(__name__)
app.secret_key = "secretKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def colninja(color):
    return render_template("ninja.html", color=color)

app.run(debug=True)
