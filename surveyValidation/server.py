from flask import Flask,redirect,request,render_template,flash


app = Flask(__name__)
app.secret_key = 'secretKey'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name) > 0 and len(comment) > 0 and len(comment) < 120:
        return render_template('result.html',name=name,location=location,language=language,comment=comment)
    else:
        if len(name) == 0:
            flash("Name cannot be empty")
        if len(comment) == 0:
            flash("Comment cannot be empty")
        if len(comment) > 120:
            flash("Comment cannot be more than 120 chars")
    return redirect('/')

app.run(debug=True)
