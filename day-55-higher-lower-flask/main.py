from flask import Flask
import random
app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapped_funcion():
        return f"<b>{function()}</b>"
    return wrapped_funcion


def make_emphasis(function):
    def wrapped_function():
        return f"<em>{function()}</em>"
    return wrapped_function


def make_underlined(function):
    def wrapped_function():
        return f"<u>{function()}</u>"
    return wrapped_function


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

random_number = random.randint(0, 9)

@app.route('/<int:user_number>')
def is_right(user_number):
    if user_number > random_number:
        return '<h1 style="color: red" >you are too HIGH</h1>' \
               '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    elif user_number < random_number:
        return '<h1 style="color: green">you are too LOW</h1>' \
               '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    else:
        return '<h1 style="color: blue">YOU ARE RIGHT</h1>' \
               '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)


