import streamlit as st
st.title("Hello, Streamlit! My web app")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Learning Streamlit for the first time")



agree = st.checkbox("I agree with Hima,Teju,Ayu")

if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    ["Mathu vadalara 2[Comedy]", "GOAT", "Pushpa2"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == "Mathu vadalara 2[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("Great! Ayan you have selected the right one..Awesome!")
