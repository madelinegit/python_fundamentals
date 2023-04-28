from flask import Flask, render_template, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

#Root Route
@app.route('/')
def index():
    if 'count' in session:
        print('key exists!')
        count=session['count']
    else:
        print("key 'count' does NOT exist")
        count=0
    count+=1
    print(count)
    session['count'] = count
    #creates a key/value pair, operates like a dictionary
    return render_template('index.html', count=session['count'])
#left=html-name right=py-name
#function, expression

#check if the key "count" is in session, start at 0 if not, or keep going

# @app.route('/count')
# def counting():
#     count=session['count']
#     #grab it from session so that this function will know whats going on
#     count+=1
#     session['count'] = count
#     #put it back into session
#     print ("You are counting", count)
#     return redirect('/')
@app.route('/two')
def two_visits():
    if 'count' in session:
        print('key exists!')
        count=session['count']
    else:
        print("key 'count' does NOT exist")
        count=0
    count=count+1
    print(count)
    session['count'] = count
    return redirect('/')


#button to reset the counter
@app.route('/destroy')
def destroy_session():
    session.clear()		# clears all keys
    return redirect('/')

# @app.route('/clear_unicorn')
# def clear_entire_session():
#     session.clear()
#     return redirect('/')

# arr=[]
# for i in range (0, len(arr)):
#     i++
#     append.arr()

# def count_up(low, max):
#     while low <= max:
#         print(low)
        # low += 1

# @app.route('/')
# def counter():
#     counter.num += 1
#     print("Number of visits:", counter.num)
#     return render_template('/', number = num )

if __name__ =='__main__':
    app.run(debug=True)