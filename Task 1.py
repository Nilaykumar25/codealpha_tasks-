'''Language Translation Tool
Develop a simple language translation tool that
translates text from one language to another. Use
machine translation techniques and pre-trained
models like Google Translate API or Microsoft
Translator API to translate text.'''


import requests

def translate_text(text, source_lang, target_lang, api_key):
    """
    Translates text from source language to target language using Google Translate API.

    Parameters:
        text (str): The text to translate.
        source_lang (str): The source language code (e.g., 'en' for English).
        target_lang (str): The target language code (e.g., 'es' for Spanish).
        api_key (str): Your Google Cloud Translate API key.
    """
    url = "https://translation.googleapis.com/language/translate/v2"
    headers = {"Content-Type": "application/json"}
    data = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "key": api_key,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            translated_text = response.json()["data"]["translations"][0]["translatedText"]
            return translated_text
        except KeyError:
            return "Error: Unexpected response format."
    else:
        try:
            error_message = response.json()["error"]["message"]
            return f"Error: {response.status_code}, {error_message}"
        except KeyError:
            return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    # Get user inputs
    api_key = input("Enter your Google Translate API key: ")
    text = input("Enter text to translate: ")
    source_lang = input("Enter the source language code (e.g., 'en' for English): ")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    # Translate the text
    translated_text = translate_text(text, source_lang, target_lang, api_key)

    # Display the result
    print("Translated Text:", translated_text)
