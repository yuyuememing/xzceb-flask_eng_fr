#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#apikey = os.environ['apikey']
#url = os.environ['url']
APIKEY='4vUIIE_2UPzKBibZ97Bo9eU-MJunw-uLdD4qRluUnwHK'
URL='https://api.us-south.language-translator.watson.cloud.ibm.com'
authenticator = IAMAuthenticator('4vUIIE_2UPzKBibZ97Bo9eU-MJunw-uLdD4qRluUnwHK')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    #This function translates English to French
    translation = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #This function translates French to English
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text