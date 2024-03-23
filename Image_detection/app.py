import streamlit as st
import cv2
import pytesseract
from googletrans import Translator
from gtts import gTTS
import os
from PIL import Image

# Set page title
st.set_page_config(page_title="Text Recognition & Translation App", layout="wide")

st.title("Text Recognition & Translation App")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to text
    text = pytesseract.image_to_string(image)
    st.subheader("Extracted Text:")
    st.write(text)

    # Language selection for translation
    lang = st.selectbox("Select Language for Translation", ["en", "hi", "mr", "gu"])

    # Translation dictionary
    lang_dict = {"en": "English", "hi": "Hindi", "mr": "Marathi", "gu": "Gujarati"}

    if lang != "en":
        # Translate text
        translator = Translator()
        translated_text = translator.translate(text, dest=lang).text
    else:
        translated_text = text

    st.subheader("Translated Text:")
    st.write(translated_text)

    # Convert text to speech
    if st.button("Convert Text to Speech"):
        tts = gTTS(translated_text, lang=lang)
        tts.save("output_audio.mp3")

        # Play the audio
        audio_file = open("output_audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
