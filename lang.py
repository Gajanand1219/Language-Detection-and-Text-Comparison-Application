
from flask import Flask, request, render_template
from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
import time

app = Flask(__name__)

# Set seed for consistent language detection results
from langdetect import DetectorFactory
DetectorFactory.seed = 0

# Language code to full name mapping
LANGUAGE_MAP = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'hi': 'Hindi',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ru': 'Russian',
    'mr': 'Marathi',
    # Add more language codes and their names as needed
}

@app.route('/')
def index():
    return render_template('lang.html')

@app.route('/detect', methods=['GET','POST'])
def detect_language():
    input_text = request.form['text']  # Get text from form

    try:
        detected_languages = detect_langs(input_text)
        detected_languages_list = []
        for lang in detected_languages:
            lang_code = lang.lang
            lang_name = LANGUAGE_MAP.get(lang_code, lang_code)
            detected_languages_list.append(f"This is ({lang_code}) {lang_name} language with probability {lang.prob*100:.2f}%")
        hi = ', '.join(detected_languages_list)
    except LangDetectException:
        hi = "Could not detect the language. Please provide more input."
    time.sleep(1.6)
    return render_template('lang.html', hi=hi)

def calculate_accuracy(text1, text2):
    matches = 0
    max_length = max(len(text1), len(text2))  # Length of the longer text

    # Count matching characters
    for i in range(min(len(text1), len(text2))):
        if text1[i] == text2[i]:  # Compare characters directly
            matches += 1

    return (matches / max_length) * 100 if max_length > 0 else 0  # Calculate accuracy

@app.route('/text', methods=['GET','POST'])
def compare_text():
    result = ""
    accuracy = 0

    text1 = request.form.get('text1')
    text2 = request.form.get('text2')

    # Convert both texts to lowercase for case-insensitive comparison
    lower_text1 = text1.lower() if text1 else ''
    lower_text2 = text2.lower() if text2 else ''

    # Check if texts are identical
    if lower_text1 == lower_text2:
        result = "The texts are identical (case insensitive)."
    else:
        result = "The texts are different (case insensitive)."

    # Calculate accuracy
    accuracy = calculate_accuracy(lower_text1, lower_text2) 

    return render_template('compare.html', result=result, accuracy=round(accuracy,2))

if __name__ == '__main__':
    app.run(debug=True)
