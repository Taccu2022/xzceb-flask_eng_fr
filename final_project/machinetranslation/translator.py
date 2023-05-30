"""
translator.py: Module for language translation using IBM Watson Language Translator service.
"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_translator_instance():
    """
    Creates an instance of the IBM Watson Language Translator.

    Returns:
        LanguageTranslatorV3: The Language Translator instance.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator

def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator service.

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    language_translator = create_translator_instance()
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator service.

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    language_translator = create_translator_instance()
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
