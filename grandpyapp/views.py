from flask import Flask, render_template, url_for, request, jsonify
from mediawiki import MediaWiki
from stop_words import get_stop_words, safe_get_stop_words
import requests
import urllib.request, urllib.parse, urllib.error
import googlemaps
import json

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/get_word')
def get_prediction():
    wikipedia = MediaWiki()
    word = request.args.get('word')
    stop_words = get_stop_words('fr')
    stop_words = get_stop_words('french')
    print(stop_words)

    # split query
    filtered_sentence = ""
    filtered_sentence = word.split()

    reponse = []
    print(filtered_sentence)
    for each in filtered_sentence:
        print(each)
        if each not in stop_words:
            reponse.append(each)
            print(reponse)

    string_query = ' '.join(reponse)

    # serviceurl = 'https://www.google.com/maps/embed/v1/place?'
    """serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    while True:
        address = string_query

        "if len(address) < 1:
            break

        url = serviceurl + "key=" + app.config['KEY_API'] + "&" + urllib.parse.urlencode({'address': address})
        print('retrieving', url)

        uh = urllib.request.urlopen(url)
        data = uh.read().decode()

        try:
            js = json.loads(data)
            print(js)
        except:
            js = None
            # search_json = None

        if not js:
            if 'status' not in js:
                if js['status'] != 'OK':
                    print('==== Failure To Retrieve ====')
                    print(js)
                    continue

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]

        print('lat', lat, 'lng', lng)"""

    """location = js['results'][0]['formatted_address']

        print(location)"""

    # print(string_query)
    
    lat = '48.856614'
    lng = '2.3522219'
    query = wikipedia.geosearch(lat, lng)
    print(wikipedia.geosearch(lat, lng))

    history = query[0]

    print(history)
    print(wikipedia.summary(history))
    summary = wikipedia.summary(history)
    return jsonify({'html': summary})


if __name__ == "__main__":
    app.run(debug=True)
