from flask import Flask, request, redirect, render_template, session

import random

app = Flask(__name__)

app.secret_key = "Py is Life"

@app.route('/')
def index():
    if 'donation' and 'message' not in session:
        session['message']=[]
        session['donation'] = 0
    return render_template('index.html')
#if there isnt an existing session, then start from 0



@app.route('/adopt', methods=['POST'])
def adopt():
    if 'cat' == request.form['pet']:
        adoption = random.randint(10, 30)
        session['donation'] += adoption
        print(adoption)
        session['message'].append(f'Congratulations on your pet and thank you for your donation.')
        return redirect('/')

    if 'dog' == request.form['pet']:
        adoption = random.randint(30,50)
        session['donation'] += adoption
        session['message'].append(f'Congratulations on your pet and thank you for your donation.')
        return redirect('/')

    if 'bird' == request.form['pet']:
        adoption = random.randint(15,20)
        session['donation'] += adoption
        session['message'].append(f'Congratulations on your pet Cat and thank you for your donation.')
        return redirect('/')

    if 'donation' == request.form['pet']:
        adoption = random.randint(0,75)
        session['donation'] += adoption
        session['message'].append(f'Thank you for your donation.')
        return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)