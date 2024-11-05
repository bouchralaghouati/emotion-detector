import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json = myobj, headers=header)
    
    formatted_response = json.loads(response.text)
  
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotion_data['anger']
    disgust = emotion_data['disgust']
    fear = emotion_data['fear']
    joy = emotion_data['joy']
    sadness = emotion_data['sadness']

    dominant_emotion = max(emotion_data, key=emotion_data.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }