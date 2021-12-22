from flask import Flask
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
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR48ivSfj5ffrq25JXBzNVE-3kbvHxEVKeDUw&usqp=CAU">'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

@app.route('/<name>')
def say_name(name):
    return f"Hello you {name}"

if __name__ == "__main__":
    app.run(debug=True)


