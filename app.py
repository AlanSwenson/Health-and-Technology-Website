from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:user>')
def user(user):
    return f"What up {user}"


if __name__ == '__main__':
    app.run(debug=True)