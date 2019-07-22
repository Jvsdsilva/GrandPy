from flask import Flask, render_template, url_for, request
from stop_words import get_stop_words
from stop_words import safe_get_stop_words
from mediawiki import MediaWiki

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')

def index():
    #query = request.args.get('query')
    #url='https://en.wikipedia.org/wiki/'+ str(query)

    print(query)
    #print(url)
    #wikipedia = MediaWiki()

    #print(wikipedia.search('washington'))
    #print(wikipedia.geosearch(title='washington, d.c.'))

    return render_template('base.html')

@app.route('/echo/', methods=['POST'])
def echo():
    """stop_words = get_stop_words('fr')
    stop_words = get_stop_words('french')
    stop_words = safe_get_stop_words('unsupported language')"""
    # stop word set language
    #stop_words = stopwords.stopwords("fr")  # Frech stopwords
    # query
    #example_sent = " b"
    # split query
    #filtered_sentence = ""
    
    """for w in filtered_sentence: 
        if w not in stop_words: 
            filtered_sentence.append(w) """
    
    return render_template('base.html', query=request.form['text'])


if __name__ == "__main__":
    app.run()
