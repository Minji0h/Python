from flask import Flask, render_template, url_for
from loginForm import LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "oh-sehunnie"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


@app.route('/login/success')
def success_login():
    return render_template("success.html")


@app.route('/login/denied')
def denied_access():
    return render_template("denied.html")


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)