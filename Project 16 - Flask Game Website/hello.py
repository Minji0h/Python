from flask import Flask
import random

app = Flask(__name__)

num = random.randint(1,10)


@app.route('/')
def home():
    return '<h1 style="text-align:center">Guess a number between 0 and 9</h1>'\
            '<center><iframe src="https://giphy.com/embed/l378khQxt68syiWJy" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></center>'

@app.route('/<int:number>')
def numbers(number):
    if number < num:
        return f'<h1 style="text-align:center">The number {number} is too low!</h1>' \
               '<center><iframe src="https://giphy.com/embed/2sfEg0Yv4c8E5VT7s3" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></center>'

    elif number > num:
        return f'<h1 style="text-align:center">The number {number} is too high!</h1>' \
               '<center><iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="480" height="453" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></center>'

    else:
        return f'<h1 style="text-align:center">You found me!</h1>' \
               '<center><iframe src="https://giphy.com/embed/yWAJmLu7un7BV2I46i" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></center>'

if __name__=="__main__":
    app.run()

