
import os
import urllib3
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
urllib3.disable_warnings()
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


def instantiate_translator():
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    language_translator.set_disable_ssl_verification(True) 
    return language_translator


def english_to_french(english_text):
    #write the code here
    language_translator = instantiate_translator()
    try:
        response = language_translator.translate(text=english_text, model_id="en-fr").get_result()
        french_text = response["translations"][0]["translation"]
        return french_text
    except ApiException:
        return ""


def french_to_english(french_text):
    #write the code here
    language_translator = instantiate_translator()
    try:
        response = language_translator.translate(text=french_text, model_id="fr-en").get_result()
        english_text = response["translations"][0]["translation"]
        return english_text
    except ApiException:
        return ""
    