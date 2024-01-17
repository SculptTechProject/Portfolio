import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mateusz Dalke")
    content = """
    👋 Hello, I'm Mateusz, a passionate learner and aspiring developer. 
    Welcome to my portfolio, 
    where I showcase my journey in the world of programming.
    """
    st.info(content)

    content1 = """
    I am currently immersed in the realms of Python and C#, 
    driven by a relentless curiosity and eagerness to create innovative solutions. 
    The ever-evolving nature of technology keeps me on my toes, 
    and I thrive on the challenges it presents.
    """
    st.info(content1)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contant me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")