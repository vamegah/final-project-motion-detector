import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the motiom detector API
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    json_payload = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, json = json_payload, headers = header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Extract the required emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare the output in the required format
    formated_dictected_emotions = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }


    # Return the detected motion
    return formated_dictected_emotions