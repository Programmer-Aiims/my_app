import streamlit as st
from PIL import Image
import numpy as np

imgbuffer = st.camera_input('cam')

if imgbuffer:
    img = Image.open(imgbuffer)
    imgnp = np.array(img)
    st.write(imgnp.shape)
