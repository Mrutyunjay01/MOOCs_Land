from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    conferences = ["ICCV", "NIPS", "EUSIPCO"]
    return render_template('index.html', conferences=conferences)
    pass


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    pass
