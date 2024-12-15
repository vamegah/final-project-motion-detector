''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detection function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_detector():

    # Retrieve the text to detect from the request arguments
    text_to_detect = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_detect)
    
    # Return a formatted string with the emotions
    return  (
        f"For the given statement, the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')}, "
        f"and 'sadness': {response.get('sadness')}. "
        f"The dominant emotion is {response.get('dominant_emotion')}."
    )


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 500)