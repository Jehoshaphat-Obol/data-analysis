import streamlit as st

class Layout:
    def __init__(self, title, introduction="", image="", description=""):
        self.title = title
        self.introduction = introduction
        self.image = image
        self.description = description
        
    def render(self):
        st.title(self.title)
        st.write(self.introduction)
        if self.image != "":
            st.image(self.image)
        st.write(self.description)