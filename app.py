from flask import Flask, render_template

app = Flask(__name__)

HER_NAME = "Her Name Here"

@app.route("/")
def home():
    return render_template("index.html", name=HER_NAME)

@app.route("/celebrate")
def celebrate():
    return render_template("celebrate.html", name=HER_NAME)

@app.route("/gift")
def gift():
    return render_template("gift.html", name=HER_NAME)

if __name__ == "__main__":
    app.run(debug=True)