import streamlit as st
st.title("My Calculator")

def square(x):
    return x*x



number = st.number_input("Insert a number")
st.write(number)


if st.button("Get square"):
    res = square(number)
    st.header(res)
    