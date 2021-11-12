from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World 10"

@app.route('/hello')
def hello():
    return render_template("hello.html")


if __name__ == '__main__':
    app.run(debug=True)