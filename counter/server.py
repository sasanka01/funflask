from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'mySecret'
@app.route('/')
def index():
    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    session['count'] = 0
    return redirect('/')


app.run(debug=True)
