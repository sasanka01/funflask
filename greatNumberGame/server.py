from flask import Flask,session,redirect,request,render_template
import random
app = Flask(__name__)
app.secret_key = 'mySecret'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,101)
        session['message'] = ""
        session['guess'] = ""
    print session['number']
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
    if session['number'] == int(request.form['guess']):
        session['message'] = "you have guessed it right. play agian"
        return redirect('/reset')
    elif session['number'] < int(request.form['guess']):
        session['message'] = "You have guessed it high, guess something lower"
    elif session['number'] > int(request.form['guess']):
        session['message'] = "You have guessed it low, guess something higher"
    return render_template('index.html',message=session['message'])


@app.route('/reset')
def reset():
    session.pop('number')
    return redirect('/')



app.run(debug=True)
