from flask import Flask, render_template, jsonify, request
from model import db, connect_to_db, Card

app = Flask(__name__)


DATA = {"cards":
            [{
              "name": "Balloonicorn",
              "skill": "video games",
              "imgUrl": "/static/img/balloonicorn.jpg"
            },

            {
              "name": "Float",
              "skill": "baking pretzels",
              "imgUrl": "/static/img/float.jpg"
            },

            {
              "name": "Llambda",
              "skill": "knitting scarves",
              "imgUrl": "/static/img/llambda.jpg"
            },

            {
              "name": "Off-By-One",
              "skill": "climbing mountains",
              "imgUrl": "/static/img/off-by-one.jpg"
            },

            {
              "name": "Seed.py",
              "skill": "making curry dishes",
              "imgUrl": "/static/img/seedpy.jpg"
            },

            {
              "name": "Polymorphism",
              "skill": "costumes",
              "imgUrl": "/static/img/polymorphism.jpg"
            },

            {
              "name": "Short Stack Overflow",
              "skill": "ocean animal trivia",
              "imgUrl": "/static/img/shortstack-overflow.jpg"
            },

            {
              "name": "Merge",
              "skill": "bullet journaling",
              "imgUrl": "/static/img/merge.jpg"
            }]
}

@app.route("/")
def show_homepage():
    """Show the application's homepage."""

    return render_template("homepage.html")

@app.route("/cards")
def show_cards():
    """Show all trading cards."""

    return render_template("cards.html")

@app.route("/cards.json")
def get_cards_json():
    """Return a JSON response with all cards in DB."""

    cards = Card.query.all()
    cards_list = []

    for c in cards:
        cards_list.append({"skill": c.skill, "name": c.name, "imgUrl": c.image_url})


    return jsonify({"cards": cards_list})

@app.route("/add-card", methods=["POST"])
def add_card():
    """Add a new card to the DB."""

    name = request.form.get('name')
    skill = request.form.get('skill')

    new_card = Card(name=name, skill=skill)
    db.session.add(new_card)
    db.session.commit()

    return jsonify({"success": True})

@app.route("/cards-jquery")
def show_cards_jquery():
    return render_template("cards-jquery.html")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
