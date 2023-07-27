# streamlit_app.py

import pandas as pd
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
