from flask import Flask, render_template, request, redirect, session
#render_template, request, redirect, session
app = Flask(__name__)
#import flast to allow us to create our app
#create a new instance of the Flask class called "app"

app.secret_key = "This is a secret"

@app.route('/')
def index():
# if 'submitted_forms' not in session:
#     session['submitted_forms']=[]
    return render_template('index.html')



@app.route('/result', methods= ['post'])
def result_page():
    print("we got in")
    print(request.form)
    print(request.form["dojo_location"])
    session['your_name'] = request.form['your_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    print(session)
    # print(session['your_name', 'dojo_location', 'fav_language', 'comment'])
    #return render_template('result.html', name = session['your_name'], location = session['dojo_location'], favorite = session['fav_language'], comment = session['comment'], users = session('submitted_forms'))
    return redirect ("/result")

@app.route('/result')
def result():
    print(session)
    return render_template("result.html")

@app.route('/clear_unicorn')
def clear_entire_session():
    session.clear()
    return redirect('/')

@app.route('/clear_comment')
def clear_comment():
    session.pop('comment')
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)