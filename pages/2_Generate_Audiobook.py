import streamlit as st

st.title('🗣️ ParentParrot: Generate Audiobook')


st.header('Upload Text File')
#text_file = st.file_uploader("Choose a TXT file", type="txt")
text_option = st.radio('Choose an option:', ('Upload a text file', 'Write text here'))

if text_option == 'Upload a text file':
    text_file = st.file_uploader("Choose a TXT file", type="txt")
    if text_file is not None:
        ext = text_file.read().decode()
else:
    text = st.text_area('Write your text here:')

st.header('Upload Voice Sample')
voice_file = st.file_uploader("Choose an MP3 file", type="mp3")
if voice_file is not None:
    voice_sample = voice_file.read()

if st.button('Generate Audiobook'):
    if text_file is not None and voice_file is not None:
        st.write('Cloning voice...')
        #cloned_voice = clone_voice(voice_sample)

        st.write('Converting text to speech...')
        #speech = text_to_speech(text, cloned_voice)

        st.write('Generating audiobook...')
        #audiobook = generate_audiobook(speech)

        st.write('Audiobook generated successfully!')
        st.audio(audiobook, format='audio/mp3')
    else:
        st.write('Please upload both a text file and a voice sample.')