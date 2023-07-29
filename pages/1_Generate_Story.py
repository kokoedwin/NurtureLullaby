import streamlit as st
import os
from dotenv import load_dotenv
import openai

st.title('🗒️ NurtureLullaby: Generate Your Story')

#option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))


# Load environment variables from .env file
load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv('CHATGPT_API_KEY')

def generate_story(prompt):
    # Generate a story using ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Return the assistant's reply
    return response['choices'][0]['message']['content']

def main():
    st.title('NurtureLullaby: Create Your Story')

    st.header('Enter Your Story Prompt')
    prompt = st.text_input('Start your story...')

    if st.button('Generate Story'):
        if prompt:
            st.write('Generating story...')
            story = generate_story(prompt)
            st.write(story)
        else:
            st.write('Please enter a story prompt.')

if __name__ == "__main__":
    main()