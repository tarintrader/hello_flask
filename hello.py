from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold

def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"
    return emphasis

def make_underlined(function):
    def underlined():
        return f"<u>{function()}</u>"
    return underlined

@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img src='https://media.giphy.com/media/CkMnLcOgKOxfa/giphy.gif' width=200>")


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
