import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and its fifth power")

# get user input
n = st.number_input("Enter an integer", value=1, step=1)

# calculate square, cube and fifth power
square = n ** 2

cube = n ** 3

fifth_power = n ** 5

# display results

st.write(f"Square of {n} is: {square}")

st.write(f"Cube of {n} is: {cube}")

st.write(f"Fifth power of {n} is: {fifth_power}")