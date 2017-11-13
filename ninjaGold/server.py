from flask import Flask,session,redirect,render_template,request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "mySecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['log'] = []
    return render_template('index.html',gold=session['gold'],log=session['log'])



@app.route('/process_money',methods=['POST'])
def money():
    time = datetime.now()
    print time
    if request.form['building'] =='farm':
        result = random.randint(10,20)

    elif request.form['building'] =='cave':
        result = random.randint(5,10)

    elif request.form['building'] =='house':
        result = random.randint(2,5)

    elif request.form['building'] =='casino':
        result = random.randint(-50,50)

    message = "you have won/lost {} Gold at {}".format(result,datetime.now().strftime("%H:%M"))
    session['gold'] = int(session['gold']) + result
    Log = session['log']
    Log.append(message)
    return redirect('/')


app.run(debug=True)
