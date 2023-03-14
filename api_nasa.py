import streamlit as st
import requests


api_key = 'byKJojVf2OQeRXgqDrotqzoMTRmoGiZ5g70fjGhY'
url = 'https://api.nasa.gov/planetary/apod?' \
      f'api_key={api_key}'

# Get a request data as a dictionary
response1 = requests.get(url)
data = response1.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

image_filepath = 'img.png'
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)


st.title(title)
st.image(image_filepath)
st.write(explanation)