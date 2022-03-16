import streamlit as st


def change_keyboard(s):
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    rus = "йцукенгшщзхъфывапролджэячсмиьбю."
    tranlation = {e: r for (e, r) in zip(en, rus)}
    new_s = [tranlation.get(elem, elem) for elem in s]
    return "".join(new_s)

st.title("#First app")
text_input = st.text_input("Input english text here")
st.write(change_keyboard(text_input))