"""A madlib game that compliments its users."""

from random import choice

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

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_madlib_form():
    """Enter madlib game info """ 
    
    game_choice = request.args.get("game")
    

    if game_choice == 'yes':
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib_game')
def play_madlibs():
    """Play madlib game """ 
    
    name = request.args.get("madlib-name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    box = request.args.get("box")
    cat_call = request.args.get("cat_call")
    madlib_choice =choice(["madlib_game.html", "madlib_game2.html", "madlib_game3.html"])


    return render_template(madlib_choice, person=name, color=color, noun=noun, adjective=adjective, box=box, cat_call=cat_call)        




if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
