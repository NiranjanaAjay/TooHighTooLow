from flask import Flask
import random

app = Flask(__name__)

COLOURS = ['violet','indigo','blue','green','yellow','orange','red']
RESULT = random.randint(0,9)

def random_colour(function,**kwargs):
    def wrapper(**kwargs):
        ran_colour = random.choice(COLOURS)
        return f'<h1 style="color:{ran_colour}">{function(**kwargs)}</h1>'
    return wrapper

@app.route('/')
def home_page():
    return "<h1>Guess a number between 0 and 9 ;)</h1>"

@app.route("/<int:num>")
@random_colour
def guess_page(num):
    if num == RESULT:
        return "YOU'VE GUESSED IT RIGHT! :)"
    elif num > RESULT:
        return "TOO HIGH! :("
    else:
        return "TOO LOW! :("


app.run(debug=True)