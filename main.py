import json
from random import randrange
from googletrans import Translator
from flask import ( Flask, render_template )
from os import getenv
from dotenv import load_dotenv
load_dotenv()

translator = Translator()
app = Flask(__name__)

to_translate = getenv("TO_TRANSLATE").capitalize()

file = open("languages.json", "r")
languages = json.loads(file.read())
file.close()
count = len(languages)

@app.route('/')
def index():
    language = languages[randrange(count)]

    translation = translator.translate(to_translate, src="en", dest=language['code'])
    
    return render_template('translator.html', original=to_translate, language_to=language["name"], language_to_link=language["link"], translated=translation.text)

@app.route('/api')
def api():
    language = languages[randrange(count)]

    translation = translator.translate(to_translate, src="en", dest=language['code'])
    
    return {
        "language": language,
        "translation": {
            "original": to_translate,
            "translated": translation.text
        }
    }
    
if __name__ == '__main__':
    app.run()