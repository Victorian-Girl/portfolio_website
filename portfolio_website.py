import streamlit as st                                                                  # Importing Streamlit
import google.generativeai as genai                                                     # Importing the GenAI library

api_key = st.secrets["GOOGLE_API_KEY"]                                                  # Getting the API key from the secrets
# api_key =""
genai.configure(api_key=api_key)                                                        # Configuring the GenAI library
model = genai.GenerativeModel('gemini-1.5-flash')                                       # Creating a GenerativeModel object


col1, col2 = st.columns(2)                                                              # Creating 2 columns in the layout

with col1:                                                                              # Adding content to the first column
    st.subheader("Hi :wave:")                                                           # Adding a subheader
    st.title("I am Mélissa Christiaenssens")                                            # Adding a title

with col2:                                                                              # Adding content to the second column
    st.image("images/moi-8.png")                                                        # Adding an image

st.title(" ")


persona = """
        You are Mélissa AI bot. You help people answer questions about your self (i.e Mélissa)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """


st.title("Mélissa's AI Bot")                                                            # Adding a title

user_question = st.text_input("Ask anything about me")                                  # Adding a text input
if st.button("ASK", use_container_width=400):                                           # Adding a button
    prompt = persona + "Here is the question that the user asked: " + user_question     # Creating the prompt
    response = model.generate_content(prompt)                                           # Generating the response
    st.write(response.text)                                                             # Displaying the response

st.title(" ")                                                                           # Adding a blank space

col1, col2 = st.columns(2)                                                              # Creating 2 columns in the layout
with col1:                                                                              # Adding content to the first column
    st.subheader("My artist web site")                                                  # Adding a subheader
    st.write("- Made with Adobe Illustrator")                                           # Adding a text
    st.write("- And a wonderfully app name Svija")                                      # Adding a text
    st.write("- Come see my art")                                                       # Adding a text
    st.write("- Know me better")                                                        # Adding a text
    st.write("- I'm am a programmer, but also a artist")                                # Adding a text

with col2:                                                                              # Adding content to the second column
    st.write("https://mcrist.artiste.svija.site/")                                      # Adding a video
    st.image("images/site_2.png")                                                       # Adding an image

st.title(" ")                                                                           # Adding a blank space, peut aussi utiliser st.subheader(" "), st.write(" "), st.markdown(" ")

st.title("My Setup")                                                                    # Adding a title
st.image("images/setup.jpg")                                                            # Adding an image

st.write(" ")
st.title("My Skills")                                                                   # Adding a title
st.slider("Programming", 0, 100, 55)                                                    # Adding a slider
st.slider("Painting", 0, 100, 75)                                                       # Adding a slider
st.slider("Studying", 0, 100, 80)                                                       # Adding a slider

st.write(" ")
st.title("Gallery")                                                                     # Adding a title

col1, col2, col3 = st.columns(3)                                                        # Creating 3 columns in the layout

with col1:                                                                              # Adding content to the first column
    st.image("images/g.jpg")                                                           # Adding an image
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")

with col2:                                                                              # Adding content to the second column
    st.image("images/g3.jpg")                                                           # Adding an image
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")

with col3:                                                                              # Adding content to the third column
    st.image("images/g7.jpg")                                                           # Adding an image
    st.image("images/g3.jpg")
    st.image("images/g8.jpg")

st.subheader(" ")                                                                       # Adding a subheader
st.write("CONTACT")                                                                     # Adding a text
st.title("For any inquiries, email at:")                                                # Adding a title
st.subheader("metalomax@gmail.com")                                                     # Adding a subheader
