import streamlit as st
import pdfplumber
from googletrans import Translator

# Streamlit UI
def main():
    st.set_page_config(page_title="PDF Translator", page_icon="📚", layout="wide")

    # Include CSS styles
    st.markdown(
        """
        <style>
            body {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: Arial, sans-serif;
            }

            .st-bv {
                margin-left:10px;
                padding:2px 15px;
                border-radius: 0.5rem;
                background-color: #332f45;
                
            }

            .st-bv.st-dx {
                box-shadow: none;
                cursor:pointer;
            }

            .st-bv.st-dx:not(:last-child) {
                margin-bottom: 0px;
            }

            .stSelectbox select {
                background-color: #4a427f;
                color: #ffffff;
                cursor:pointer;
            }

            .stSelectbox select:hover {
                background-color: #665ca0;
                cursor:pointer;
            }

            .stSelectbox select:focus {
                background-color: #665ca0;
                cursor:pointer;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("PDF Translator")
    st.write("Upload a PDF file and select the language you want to translate the text into.")

    # File uploader
    uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])

    # Language selection
    target_lang = st.selectbox("Select Language for Translation", ["English", "Hindi", "Marathi", "Gujarati", "Tamil", "Bengali"])

    lang_code_mapping = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Tamil":"tm",
        "Bengali": "bn"
    }

    if uploaded_file:
        st.write("Original PDF Text:")
        
        # Initialize translator
        translator = Translator()

        # Open PDF file using pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            # Iterate through each page of the PDF
             for page in pdf.pages:
                try:
                    # Extract text from the current page
                    text = page.extract_text()

                    # Translate the extracted text to the selected language
                    translated_text = translator.translate(text, dest=target_lang.lower()).text

                    # Display the translated text
                    st.write("Translated PDF Text:")
                    st.write(translated_text)

                    # Write the translated text to a file
                    with open("translated_text.txt", mode='a', encoding='utf-8') as txt_file:
                        txt_file.write(translated_text + '\n')
                except Exception as e:
                    # Skip to the next page if an exception occurs (e.g., null boxes)
                    st.warning(f"Error on page {page.page_number}: {e}")
                    continue

# Run the Streamlit app
if __name__ == "__main__":
    main()
