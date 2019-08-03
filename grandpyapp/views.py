from flask import Flask, render_template, url_for, request, jsonify
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
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
# Initialize the extension
GoogleMaps(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/get_word')
def get_prediction():
    wikipedia = MediaWiki()
    word = request.args.get('word')
    # Set stop words language
    stop_words = get_stop_words('en')
    stop_words = get_stop_words('english')

    # split query
    filtered_sentence = ""
    filtered_sentence = word.split()

    reponse = []

    for each in filtered_sentence:
        if each not in stop_words:
            reponse.append(each)
            print(reponse)

    string_query = ' '.join(reponse)

    """serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    while True:
        address = string_query

        if len(address) < 1:
            break
        
        try:
            url = serviceurl + "key=" + app.config['KEY_API'] + "&" + urllib.parse.urlencode({'address': address})
            print('retrieving', url)
            
            uh = urllib.request.urlopen(url)
            data = uh.read().decode()
            js = json.loads(data)
            #print(js)
        except e:
            print('==== Failure To Retrieve ===='+ e)
            js = None
            #print(js)
        
        if not js:
            if 'status' not in js:
                if js['status'] != 'OK':
                    print('==== Failure To Retrieve ====')
                    print(js)
                    continue
        else:
            lat = js["results"][0]["geometry"]["location"]["lat"]
            lng = js["results"][0]["geometry"]["location"]["lng"]

            print('lat', lat, 'lng', lng)"""

            # print(string_query)
            
    lat = '48.856614'
    lng = '2.3522219'

    # sent coordinates to Media wiki
    query = wikipedia.geosearch(lat, lng)

    # Save first answer
    history = query[0]

    # sent answer to Media wiki
    summary = wikipedia.summary(history)

    # return summary to view html
    return jsonify({'html': summary})
    
@app.route('/get_coord')
def get_coordinates():
    latlng = []
    reponse = []
    word = request.args.get('word')
    # Set stop words language
    stop_words = get_stop_words('en')
    stop_words = get_stop_words('english')

    # split query
    filtered_sentence = ""
    filtered_sentence = word.split()

    for each in filtered_sentence:
        if each not in stop_words:
            reponse.append(each)
            #print(reponse)

    string_query = ' '.join(reponse)

    """serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    while True:
        address = string_query

        if len(address) < 1:
            break
        try:
            url = serviceurl + "key=" + app.config['KEY_API'] + "&" + urllib.parse.urlencode({'address': address})
        except:
            print('retrieving', url)
        
        try:
            uh = urllib.request.urlopen(url)
            data = uh.read().decode()
            
        except:
            print('==== Failure To Retrieve ===='+ uh)
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
        else:
            lat = js["results"][0]["geometry"]["location"]["lat"]
            lng = js["results"][0]["geometry"]["location"]["lng"]

            print('lat', lat, 'lng', lng)"""
    
    lat = '48.856614'
    lng = '2.3522219'
    latlng.append(lat)
    latlng.append(lng)
    
    location = json.dumps(latlng)

    # Return new coordinates to reload map view html
    return jsonify({'html': location})

        
if __name__ == "__main__":
    app.run(debug=True)
