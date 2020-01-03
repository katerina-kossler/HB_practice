"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Movie, Rating


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template('homepage.html')


@app.route('/users')
def user_list():
    """Show list of users"""

    users = User.query.all()

    return render_template("user_list.html",
                            users=users)


@app.route('/users/<user_id>')
def display_user_page(user_id):
    """ still in progress """

    user = User.query.get(user_id)
    # user.email, user.zipcode, user.age, user.ratings (returns a list)
    # still in progress - can then access list of ratings with setup

    ratings = db.session.query(Movie.title,
                               Rating.score).join(Rating).all()

    # later: connect movie id to movie name > Rating.movie_id : Movie.title

    return render_template('user.html',
                           user=user,
                           ratings=ratings)


@app.route('/movies')
def movie_list():
    """Show list of movies"""

    movies = Movie.query.all()
    return render_template('movie_list.html',
                           movies=movies)


@app.route('/register', methods=['GET'])
def display_register_form():
    """Shows a form for user to add information"""

    return render_template('register_form.html')


@app.route('/register', methods=['POST'])
def register_process():
    """Processes user information"""

    email = request.form.get("email")
    password = request.form.get("password")
    age = int(request.form.get("age"))
    zipcode = request.form.get("zipcode")

    user_in_system = User.query.filter_by(email=email).first()

    if not user_in_system:
        user = User(email=email,
                    password=password,
                    age=age,
                    zipcode=zipcode)
        db.session.add(user)
        db.session.commit()

    return redirect('/')


@app.route('/login', methods=['GET'])
def display_login_form():
    """Shows the login screen that requests user email and password"""

    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def authenticate_user():
    """Compare user input information to stored users"""

    email = request.form.get("email")
    password = request.form.get("password")

    user_in_system = User.query.filter_by(email=email).first()
    password_in_system = user_in_system.password

    if (password_in_system == password):
        session['current_user'] = user_in_system.user_id
        flash('Successfully Logged in')

    return redirect('/users/{}'.format(session['current_user']))

@app.route('/logout')
def logout_user():
    """Logout a user"""

    del session['current_user']
    flash('Successfully Logged out')

    return redirect('/')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
