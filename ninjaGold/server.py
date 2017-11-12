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
        gold = random.randint(10,20)
        session['log'].append({'state':"You entered a farm and won {} golds".format(gold), 'result':'win', 'time':time})
    elif request.form['building'] =='cave':
        gold = random.randint(5,10)
        session['log'].append({'state':"You entered a cave and won {} golds".format(gold), 'result':'win', 'time':time})
    elif request.form['building'] =='house':
        gold = random.randint(2,5)
        session['log'].append({'state':"You entered a house and won {} golds".format(gold), 'result':'win', 'time':time})
    elif request.form['building'] =='casino':
        gold = random.randint(-50,50)
        if gold < 0:
            session['log'].append({'state':"You entered a casino and lost {} golds".format(gold), 'result':'loss', 'time':time})
        else:
            session['log'].append({'state':"You entered a casino and won {} golds".format(gold), 'result':'win', 'time':time})
    session['gold'] += gold
    print gold
    return redirect('/')

app.run(debug=True)
