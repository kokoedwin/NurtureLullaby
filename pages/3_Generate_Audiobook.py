import os
import requests
import streamlit as st
from dotenv import load_dotenv
from elevenlabs import clone, generate, play, set_api_key
import json

# Load environment variables from .env file
load_dotenv()

#set_api_key(os.getenv("XI_API_KEY"))
CHUNK_SIZE = 1024

#xi-api-key = os.getenv("XI_API_KEY")
headers = {
  "Accept": "application/json",
  "xi-api-key": "cd608285bc2f22ed29bb0e13f74fadee"
}

def text_to_speech(text, voice_id):
    url_tts = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    data = {
      "text": text,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
      }
    }

    response = requests.post(url_tts, json=data, headers=headers)
    audio = response.content
    return audio

def add_voice(name, description, file1):
    url_add_voice = "https://api.elevenlabs.io/v1/voices/add"
    data = {
        'name': name,
        'labels': '{"accent": "American"}',
        'description': description
    }

    files = [
        ('files', (file1.name, file1.read(), 'audio/mpeg')),
    ]

    response = requests.post(url_add_voice, headers=headers, data=data, files=files)
    return response.text

st.title('🔉 NurtureLullaby: Add Your Voice and Generate Audiobook')

st.header('Enter Voice Details')
name = st.text_input('Voice Name')
description = st.text_input('Voice Description')
file1 = st.file_uploader("Choose your recording voice in MP3 file", type="mp3")
#file2 = st.file_uploader("Choose the second MP3 file", type="mp3")

if st.button('Add Voice'):
    if name and description and file1 is not None:
        st.write('Adding voice...')
        response = add_voice(name, description, file1)
        st.write('Voice added successfully!')
        st.write(response)
    else:
        st.write('Please enter all the voice details and upload two MP3 files.')

st.header('Enter Text')
text = st.text_area('Enter your text here:')

if st.button('Generate Audiobook'):
    if text is not None:
        st.write('Cloning voice...')
        response = add_voice(name, description, file1)
        response_dict = json.loads(response)
        voice_id = response_dict["voice_id"]
        #voice_id = response.json()["voice_id"]

        st.write('Converting text to speech...')
        audio = text_to_speech(text, voice_id)

        st.write('Audiobook generated successfully!')
        st.audio(audio, format='audio/mpeg')
        st.download_button(
            label="Download Audiobook",
            data=audio,
            file_name='audiobook.mp3',
            mime='audio/mpeg'
        )
    else:
        st.write('Please upload both a text file and a voice sample.')
