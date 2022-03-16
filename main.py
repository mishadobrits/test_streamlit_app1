import streamlit as st
import os

def change_keyboard(s):
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    rus = "йцукенгшщзхъфывапролджэячсмиьбю."
    tranlation = {e: r for (e, r) in zip(en, rus)}
    new_s = [tranlation.get(elem, elem) for elem in s]
    return "".join(new_s)

import platform
st.write(platform.system() + " " + platform.release())

st.title("Title")
text_input = st.text_input("Input english text here")
st.write(change_keyboard(text_input))
text_input2 = st.text_input("Input english text here2")
st.write(change_keyboard(text_input + " " + text_input2))