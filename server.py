from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "survey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/accept', methods=['POST'])
def accept():
    print(request.form)
    session['name'] = request.form['fullname']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')



if __name__ == "__main__":
    app.run(debug=True)