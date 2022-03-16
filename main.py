import streamlit as st
import os

def change_keyboard(s):
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    rus = "йцукенгшщзхъфывапролджэячсмиьбю."
    tranlation = {e: r for (e, r) in zip(en, rus)}
    new_s = [tranlation.get(elem, elem) for elem in s]
    return "".join(new_s)


command = "apt-get install mkvmerge"
print(command)
os.system(command)

st.title("Title")
text_input = st.text_input("Input english text here")
st.write(change_keyboard(text_input))
text_input2 = st.text_input("Input english text here2")
st.write(change_keyboard(text_input + " " + text_input2))