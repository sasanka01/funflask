from flask import Flask,redirect,request,session,render_template,flash


app = Flask(__name__)
app.secret_key = 'secretKey'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("name cannot be empty")
    else:
        flash("success your name is {}".format(request.form['name']))
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html',name=name,location=location,language=language,comment=comment)
app.run(debug=True)
