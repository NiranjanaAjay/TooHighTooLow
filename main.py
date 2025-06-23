from flask import Flask
import random

app = Flask(__name__)

COLOURS = ['violet','indigo','blue','green','yellow','orange','red']
RESULT = random.randint(0,9)

@app.route('/')
def home_page():
    return ("<h1>Guess a number between 0 and 9 ;)</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGdiZ29naHl3N2ZxNnljMzY4aGkzMTdkbW"
            "5kY2tsZnF4bzUzajFpZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif'>")

@app.route("/<int:num>")
def guess_page(num):
    ran_colour = random.choice(COLOURS)
    if num == RESULT:
        return (f"<h1 style='color:{ran_colour}'>YOU FOUND MEEE! :)</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3l2dDcxNTNrbW45N3dlaW9ham55MTN"
                "iNnY4dDZ1cXMycTYzdmxrdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BMR4cgypuglVu/giphy.gif'>")
    elif num > RESULT:
        return (f"<h1 style='color:{ran_colour}'>TOO HIGH, TRY AGAIN! :(</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWUxZHJ6ZjNsNmZrdm54ZGJ2c2R2anl"
                "idHc2MGlkeGtmODhha3J1dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/yFQ0ywscgobJK/giphy.gif'>")
    else:
        return (f"<h1 style='color:{ran_colour}'>TOO LOW, TRY AGAIN! :(</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWUxZHJ6ZjNsNmZrdm54ZGJ2c2R2anl"
                "idHc2MGlkeGtmODhha3J1dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/yFQ0ywscgobJK/giphy.gif'>")

app.run(debug=True)