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
        Here is more info about Mélissa: 

        Melissa Christiaenssens is an Artist/Programmer. 
        
        She has chosen the field of computer vision in programming, and she is also a painter.
        
        She comes from a family of artists including painters, actors, and illustrators. 
        For over 24 years, she worked in the profession of blacksmithing, 
        designing various ideas and forms for works of art and blacksmithing projects.
        
        However, painting has always been present in her mind and she finally decided to embark on this artistic adventure.
        Attracted by shapes, colors and textures, she is constantly searching for new ideas and techniques. 
        Abstract art has particularly captured her attention, allowing her to give free rein to her imagination and 
        let her brushes glide on the canvas of creativity, following the paths traced by inspiration.
        In parallel, she also likes to explore other artistic styles according to her inspirations. 
        It is a wonderful way to broaden her horizons and enrich herself with different influences. 
        From realism capturing the meticulous details of landscapes and portraits, 
        to expressionism expressing her emotions in an intense and visceral way, 
        each style allows her to explore new forms of communication and tell stories through her creations.
        
        This diversity of artistic approaches allows her to remain constantly alert, to renew herself and to avoid monotony. 
        For her, art is an endless exploration, a perpetual quest for self-discovery and the world around her. 
        Her artistic journey is a rich path of experimentation, discovery and evolution, 
        each new canvas being an invitation to explore, innovate and share these emotions with the viewer.
        
        Melissa is a self-taught person, she devotes several hours per week to her learning, her knowledge, problem solving and trying new techniques.
        She has obtained programming certificates with Udemy.com and also with C.V.Zone.
        
        The opening of her YouTube channel will take place in the near future.
        
        On the programming side, Melissa has in-depth skills in Python (60%), 
        an intermediate knowledge in HTML and CSS (40%) as well as some expertise in JavaScript (25%). 
        She also uses Adobe Illustrator and Svija software for web design. 
        Her specialty and the niche she is targeting is computer vision, 
        an exciting field where she can combine her artistic talents and technical skills.
        
        Mélissa currently undergoing a career transition. 
        Mélissa available for new challenges and seeking an engaging employment opportunity.


        Mélissa's Email: mcrist.artiste@gmail.com
        Mélissa's Linkdin: https://www.linkedin.com/in/melissa-ch
        Mélissa's Github :https://github.com/Victorian-Girl
        Mélissa's Stackoverflow: https://stackoverflow.com/users/15284428/m%c3%a9lissa-ch
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
st.slider("Painting", 0, 100, 75)                                                       # Adding a slider
st.slider("Studying", 0, 100, 80)                                                       # Adding a slider
st.slider("Programming", 0, 100, 65)                                                    # Adding a slider
st.slider("Python", 0, 100, 90)                                                         # Adding a slider
st.slider("Html", 0, 100, 50)                                                           # Adding a slider
st.slider("Css", 0, 100, 50)                                                            # Adding a slider
st.slider("JavaScript", 0, 100, 35)                                                     # Adding a slider
st.slider("Adobe Ilustrator/Svija", 0, 100, 25)                                         # Adding a slider

st.write(" ")
st.title("Gallery")                                                                     # Adding a title

col1, col2, col3 = st.columns(3)                                                        # Creating 3 columns in the layout

with col1:                                                                              # Adding content to the first column
    st.image("images/g.jpg")                                                           # Adding an image
    st.image("images/g1.jpg")
    st.image("images/g7.jpg")

with col2:                                                                              # Adding content to the second column
    st.image("images/g3.jpg")                                                           # Adding an image
    st.image("images/g4.jpg")
    st.image("images/g9.jpg")

with col3:                                                                              # Adding content to the third column
    st.image("images/g2.jpg")                                                           # Adding an image
    st.image("images/g5.jpg")
    st.image("images/g8.jpg")

st.subheader(" ")                                                                       # Adding a subheader
st.write("CONTACT")                                                                     # Adding a text
st.title("For any inquiries, email at:")                                                # Adding a title
st.subheader("metalomax@gmail.com")                                                     # Adding a subheader
