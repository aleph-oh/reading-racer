"""Functions for getting text from speech"""
import json

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1

API_KEY = "xfUNxSGoR7AvqhiXgkz6GHOiJEiFUdrjDhM06gVHCGHd"
URL = (
    "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d9066bfe-a6ac-4e54"
    "-8ba9-cdcbd1ceb294"
)


def get_service():
    """Gets speech-to-text service"""
    authenticator = IAMAuthenticator(API_KEY)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(URL)
    return speech_to_text


def get_speech_recog(audio_file_path: str) -> str:
    """Return json-ified response for speech recognition on `audio_file_path`"""
    with open(audio_file_path, "rb") as audio_file_path:
        speech_to_text = get_service()
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file_path,
            content_type="audio/flac",
            word_alternatives_threshold=0.9,
            keywords=["colorado", "tornado", "tornadoes"],
            keywords_threshold=0.5,
        ).get_result()
    return json.dumps(speech_recognition_results)
