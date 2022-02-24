import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

  self.service_api_key=os.environ['apikey']
        self.service_api_url=os.environ['url']

        self.authenticator = IAMAuthenticator(self.service_api_key) #IAM Authenticator Instance
        self.language_translator=LanguageTranslatorV3(
                                    version='2018-05-01',
                                    authenticator=self.authenticator
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
