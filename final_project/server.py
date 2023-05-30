from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    # Get the English text from the request
    english_text = request.form['englishText']
    
    # Translate English to French using the translation function
    french_text = english_to_french(english_text)
    
    # Return the translated French text as a response
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    # Get the French text from the request
    french_text = request.form['frenchText']
    
    # Translate French to English using the translation function
    english_text = french_to_english(french_text)
    
    # Return the translated English text as a response
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
