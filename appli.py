import streamlit as st
st.title("Welcome to your personal calculator")
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")
num1 = st.number_input("Enter first number",step=1.0)
num2 = st.number_input("Enter second number",step=1.0)
option = st.selectbox("Choose an option",["+", "-", "*"])
st.write(f"Option: {option}")
if st.button('Press Now'):
    if (option == "+"):
        result = num1+num2
        st.write(f"Your result is: {result}")
    elif (option == "-"):
        result = num1-num2
        st.write(f"Your result is: {result}")
    else :
        result = num1*num2
        st.write(f"Your result is: {result}")
