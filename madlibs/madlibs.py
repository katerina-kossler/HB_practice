"""A madlib game that compliments its users."""

from random import choice, choices

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = choices(AWESOMENESS, k = 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Get user response to game and responds appropriately"""

    colors = ['blue', 'white', 'black', 'green', 'red', 'orange',
              'yellow', 'purple', 'brown']
    nouns = ['dog', 'cat', 'unicorn', 'radish', 'kumquat', 'hair brush',
             'empanada', 'mouse', 'cookie']
    adjectives = ['pretty', 'loud', 'firey', 'bouncy', 'obtuse', 'translucent',
                  'windy']

    play_game_response = request.args.get('playing')

    if play_game_response == "No":
        return render_template("goodbye.html")

    return render_template("game.html", colors=colors, nouns=nouns,
                           adjectives=adjectives)


@app.route('/madlib')
def show_madlib():
    """Show the resulting MadLib"""

    color = request.args.get('color_choice')
    person = request.args.get('person')
    adjectives = request.args.getlist('adjectives')
    adjective = choice(adjectives)
    nouns = request.args.getlist('nouns')
    noun = choice(nouns)


    return render_template('madlib.html', color=color, person=person,
                           adjective=adjective, noun=noun)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
