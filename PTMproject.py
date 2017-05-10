# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["DEBUG"] = True







@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
         return render_template("index.html")
         
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)