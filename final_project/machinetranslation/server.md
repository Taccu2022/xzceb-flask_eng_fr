# from flask import Flask, render_template, request
# from machinetranslation.translator import english_to_french, french_to_english

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Render the index.html template
#     return render_template('index.html')

# @app.route('/englishToFrench', methods=['POST'])
# def translate_english_to_french():
#     # Get the English text from the request
#     english_text = request.form['englishText']
    
#     # Translate English to French using the translation function
#     french_text = english_to_french(english_text)
    
#     # Return the translated French text as a response
#     return french_text

# @app.route('/frenchToEnglish', methods=['POST'])
# def translate_french_to_english():
#     # Get the French text from the request
#     french_text = request.form['frenchText']
    
#     # Translate French to English using the translation function
#     english_text = french_to_english(french_text)
    
#     # Return the translated English text as a response
#     return english_text

# if __name__ == '__main__':
#     app.run()
