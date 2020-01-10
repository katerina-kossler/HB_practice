from flask import Flask, render_template, request

from pprint import pformat
import os
import requests


app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'


API_KEY = os.environ['TICKETMASTER_KEY']


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route('/afterparty')
def show_afterparty_form():
    """Show event search form"""

    return render_template('afterparty-search-form.html')


@app.route('/afterparty/search')
def find_afterparties():
    """Search for afterparties on Eventbrite"""

    keyword = request.args.get('keyword', '')
    postalcode = request.args.get('zipcode', '')
    radius = request.args.get('radius', '')
    unit = request.args.get('unit', '')
    sort = request.args.get('sort', '')

    url = 'https://app.ticketmaster.com/discovery/v2/events'
    payload = {'apikey': API_KEY,
               'keyword': keyword,
               'postalCode': postalcode,
               'radius': radius,
               'unit': unit,
               'sort': sort}

    response = requests.get(url, params=payload)
    data = response.json()
    events = data['_embedded']['events']

    return render_template('afterparty-search-results.html',
                           pformat=pformat,
                           data=data,
                           results=events)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
