import streamlit as st
import subprocess
pipe = subprocess.run(['mkvmerge --help'], stdout=subprocess.PIPE)
text = pipe.stdout

def change_keyboard(s):
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    rus = "йцукенгшщзхъфывапролджэячсмиьбю."
    tranlation = {e: r for (e, r) in zip(en, rus)}
    new_s = [tranlation.get(elem, elem) for elem in s]
    return "".join(new_s)

st.write(text)

st.title("Title")
text_input = st.text_input("Input english text here")
st.write(change_keyboard(text_input))
text_input2 = st.text_input("Input english text here2")
st.write(change_keyboard(text_input + " " + text_input2))