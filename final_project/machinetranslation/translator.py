import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['1ZMEz1Ao6_0c01LmmcQC3V5gkwgM3NlEJGWk2Zg3LAQB']
url = os.environ['https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/59b330bd-954c-4c3a-bbc4-7c4663ed44c0']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    if english_text == "" or english_text is None:
        return "Please type or paste a word or phrase in English."
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]


def french_to_english(french_text):
    if french_text == "" or french_text is None:
        return "Please type or paste a word or phrase in French."
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]
