import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mateusz Dalke")
    content = """
    Hi, I am Mateusz. I'm learning python and C#.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contant me!
"""
st.write(content2)