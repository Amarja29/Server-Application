import streamlit as st
from fizzbuzz.controller import fizz_buzz_controller

def main():

    st.title("Fizz-Buzz Server")

    int1 = st.number_input("Enter First Integer", value=3)
    int2 = st.number_input("Enter Second Integer", value=5)
    limit = st.number_input("Enter Limit", value=100)
    str1 = st.text_input("Enter First String", value="fizz")
    str2 = st.text_input("Enter Second String", value="buzz")

    if st.button("Generate Fizz-Buzz"):
        result = fizz_buzz_controller(int1, int2, limit, str1, str2)
        st.write(result)

if __name__ == "__main__":
    main()