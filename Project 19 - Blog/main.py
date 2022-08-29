from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/869542f0d62b62ddbb0f"
    data_request = requests.get(url)
    data_posts = data_request.json()
    return render_template("index.html", data=data_posts)


@app.route('/posts/<int:id_post>')
def post(id_post):
    url = "https://api.npoint.io/869542f0d62b62ddbb0f"
    data_request = requests.get(url)
    data_posts = data_request.json()
    return render_template("post.html", data=data_posts, id_post=id_post)


if __name__ == "__main__":
    app.run(debug=True)