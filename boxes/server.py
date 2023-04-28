from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:play>')
def index(play):
    return render_template("index.html", phrase=play, num=5, color='blue')


@app.route('/<string:play>/<int:num>')
def numberbox(play, num):
    return render_template("index.html", phrase=play, num=num, color='blue')

@app.route('/<string:play>/<int:num>/<string:color>')
def colorbox(play, num, color):
    return render_template("index.html", phrase=play, num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)