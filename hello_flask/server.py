from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): #takes us to an html file
    return "Hello World!"

@app.route('/success')
def success():
    return "You have successfully rendered a page"

@app.route("/hello/<string:name>")
def hello(name):
    print(name)
    return "Hello welcome to FLASK" + name
#localhost5001/madeline

@app.route ('/<owner>/<bank>')
def owner_bank(owner, bank):
    return owner + "owns the bank of " + bank
#localhost5000/jaylen/money

@app.route('/<bank>/<int:number>')
def bank_number(bank, number):
    return bank+ "has " + number + " customers."

@app.route('/owner')
def owner():
    owner_info = [
        {"owner" : "Jalen", "bank" : "Money"},
        {"owner" : "Madeline", "bank" : "More Money"},
        {"owner" : "jake", "bank" : "More Problems"}
    ]
    return render_template()('owner.html', owners = owner_info)
#we have the ability to do our index.html

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True, PORT= 5001)




# / take us to the net page

# render template
# ("index.html", phrase="hello", times=5)	# 2 new named arguments!
# if __name__=="__main__":
#     app.run(debug=True)

