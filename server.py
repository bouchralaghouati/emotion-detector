""" This is a code for a http server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """this is a function to return detected emotions"""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return {"message": "Invalid text! Please try again!"}

    return {
    "anger": anger, 
    "disgust": disgust, 
    "fear": fear, 
    "joy": joy, 
    "sadness": sadness, 
    "dominant_emotion": dominant_emotion
    }

@app.route("/")
def render_index_page():
    """this is a function to render html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
