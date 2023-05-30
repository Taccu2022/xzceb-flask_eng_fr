from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def renderIndexPage():
    return render_template('index.html', translated_text='')

@app.route('/englishToFrench', methods=['GET', 'POST'])
def translate_english_to_french():
    if request.method == 'POST':
        english_text = request.form['englishText']
        french_text = english_to_french(english_text)
        return render_template('index.html', translated_text=french_text)
    else:
        # Handle the GET request by redirecting to the home page or returning an error message
        return redirect('/')

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    french_text = request.form['frenchText']
    english_text = french_to_english(french_text)
    return render_template('index.html', translated_text=english_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
