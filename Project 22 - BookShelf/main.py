from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)

all_books = []
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new_books.db"
db = SQLAlchemy(app)


class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False

db.create_all()


@app.route('/')
def home():
    return render_template("index.html", books_data=all_books)


@app.route("/add", methods=['POST','GET'])
def add():
    if request.method == 'POST':
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)

        return redirect(url_for("home"))
    return render_template("add.html")




if __name__ == "__main__":
    app.run(debug=True, port=2000)
