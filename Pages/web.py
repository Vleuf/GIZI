import streamlit as st

st.markdown("""
    <style>
    div[role="radiogroup"] label {
        color: white !important;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Tes Radio Button")

answer = st.radio("Pilih jawaban:", ["A", "B", "C"])

if st.button("Submit"):
    st.write("Jawaban Anda:", answer)
