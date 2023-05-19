import streamlit as st
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
import tempfile

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(temp_file.name)
    return temp_file.name

# Supported languages
languages = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'te': 'Telugu',
    'mr': 'Marathi',
    'ta': 'Tamil',
    'ur': 'Urdu',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'pa': 'Punjabi',
    'or': 'Odia',
    'as': 'Assamese',
    'mrj': 'Western Mari',
    'mni': 'Manipuri',
    'kok': 'Konkani',
    'ne': 'Nepali',
}

# Streamlit app
st.title("Translation and Text-to-Speech")
input_text = st.text_area("Enter the text to translate")

target_language = st.selectbox("Select the target language", list(languages.values()))

if st.button("Translate"):
    language_codes = list(languages.keys())
    selected_language_code = language_codes[list(languages.values()).index(target_language)]

    translated_text = translate_text(input_text, selected_language_code)
    st.subheader("Translated Text:")
    st.write(translated_text)

    audio_file = text_to_speech(translated_text, selected_language_code)
    audio_data = open(audio_file, "rb").read()
    st.audio(audio_data, format="audio/mp3")
