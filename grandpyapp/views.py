from flask import Flask, render_template, url_for, request, jsonify
from mediawiki import MediaWiki
from stop_words import get_stop_words, safe_get_stop_words

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

    """stop_words = get_stop_words('fr')
    stop_words = get_stop_words('french')
    stop_words = safe_get_stop_words('unsupported language')
    # split query
    filtered_sentence = ""
    filtered_sentence = word.split()
    print(filtered_sentence)
    for each in filtered_sentence:
        if each not in stop_words:
            print(each)
            filtered_sentence.append(each)"""

    print(wikipedia.search(word))
    print(wikipedia.geosearch(title=word))
    return jsonify({'html': word})


if __name__ == "__main__":
    app.run()
