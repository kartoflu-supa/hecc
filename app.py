from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sida69')
def sida69():
    return render_template("aukasida.html")

@app.route('/sida')
def sida():
    return render_template("svor.html")

if __name__ == "__main__":
    app.run(debug=True)
