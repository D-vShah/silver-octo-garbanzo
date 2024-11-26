import streamlit as st
import info
import pandas as pd


def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write('---')
about_me_section()
