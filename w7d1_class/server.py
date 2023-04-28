from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
#import flast to allow us to create our app
#create a new instance of the Flask class called "app"

app.secret_key = "This is a secret"

@app.route('/')
def index():
    if 'submitted_forms' not in session:
        session['submitted_forms']=[]
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def sumbit():
    print(request.form['first_name'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['dob'] = request.form['dob']
    session['city'] = request.form['city']
    session['state'] = request.form['state']
    session['zipcode'] = request.form['zipcode']
    session['submitted_forms'].append(request.form)
    return redirect('/profile_page')

@app.route('/profile_page')
def profile_page():
    print(session['first_name'])
    return render_template('profile.html', first = session['first_name'], last = session['last_name'], dob = session['dob'], city = session['city'], state = session['state'], zipcode = session['zipcode'], users = session('submitted_forms'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)