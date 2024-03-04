import streamlit as st
import pandas as pd

st.set_page_config("Portfolio - Metaverse Creator", "📚", "wide", "auto")

col1, col2 = st.columns([5,7],gap='large')

with col1:
    st.image('assets/verse.bmp')

with col2:
    st.title('Metaverse Creator')
    content = """
    Hi, I'm a Metaverse Creator who is passionate about creating and developing virtual worlds and experiences. I'm a self-taught developer and have been creating virtual worlds for over 10 years. I have a strong background in computer science and am proficient in programming languages such as Python, JavaScript, and C++. I have a strong understanding of 3D modeling and animation, and I'm skilled in using tools such as Blender, Unity, and Unreal Engine. I'm also experienced in creating virtual reality experiences and have a strong understanding of VR hardware and software. I'm passionate about creating immersive and engaging virtual worlds and experiences, and I'm excited to continue pushing the boundaries of what's possible in the metaverse.
    """
    st.info(content)


st.title('Projects')

# data = pandas.read_csv('data.csv')

def project_card(title,description,url,image):
    st.image(image)
    st.subheader(title)
    st.info(description)
    st.write('GitHub: [Source Code]('+url+'), [Live Demo](#)')


col3, col4, col5, col6 = st.columns([3,3,3,3],gap='large')