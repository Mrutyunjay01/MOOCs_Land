from flask import render_template
from app import app


@app.route('/home')
def index():
    conferences = ["ICCV", "NIPS", "EUSIPCO"]
    return render_template('index.html', conferences=conferences)
    pass


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    pass


if __name__ == '__main__':
    app.run(debug=True)
