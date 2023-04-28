from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect # added request

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    name = request.form['name']
    email = request.form['email']
    return redirect('/show')

# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info Form the Form")
    print(request.form)
    return render_template("show.html")
