from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = "myKey"

@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/ninja',methods = ['POST'])
def ninja():
    session['counter'] += 1
    return redirect ('/')

@app.route('/hacker', methods = ['POST'])
def hacker():
    session['counter'] = 0
    return redirect ('/')


app.run(debug=True)
