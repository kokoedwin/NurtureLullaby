import streamlit as st
import os
#from dotenv import load_dotenv
import openai


#option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))


# Load environment variables from .env file
#load_dotenv()
# Set OpenAI API key
openai.api_key = st.secrets["CHATGPT_API_KEY"]

def generate_story(age, gender, interests, story_type, moral, setting, characters):
    # Generate a story using ChatGPT
    # You'll need to modify this function to use these inputs in the generation process
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a short {story_type} story for a {age} year old {gender} who likes {interests}. The story should take place in {setting} and include characters like {characters}. The story should teach a lesson about {moral}."}
        ]
    )

    # Return the assistant's reply
    return response['choices'][0]['message']['content']


def main():
    st.title('NurtureLullaby: Create Your Story')

    st.header('Enter Story Details')
    age = st.number_input('Age of the Child', min_value=1, max_value=18, value=5)
    gender = st.selectbox('Gender of the Child', ['Male', 'Female'])
    interests = st.text_input('Interests of the Child (optional)')
    story_type = st.selectbox('Type of Story', ['Adventure', 'Fantasy', 'Mystery', 'Fairy Tale'])
    moral = st.text_input('Moral or Lesson of the Story')
    setting = st.text_input('Setting of the Story')
    characters = st.text_input('Characters in the Story')

    if st.button('Generate Story'):
        if age and gender and story_type and moral and setting and characters :
            #st.write('Generating story...')
            story = generate_story(age, gender, interests, story_type, moral, setting, characters)
            st.write(story)
        else:
            st.write('Please enter all the story details.')


if __name__ == "__main__":
    main()