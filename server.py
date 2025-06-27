'''
Deploy a Flask app to determine user emotion based on the text string
provided by the user.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    '''
    Retrieve the text string from the user and pass it to
    the analyzer. Eventually, a response with the confidence
    scores across all emotions and the dominant emotion will
    be returned.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    res = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return res

@app.route("/")
def render_index_page():
    '''
    Render the Index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
