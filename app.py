import streamlit as st
st.write("tds week 8 module")
a=st.number_input(" enter first number")
b=st.number_input(" enter second number")
if b==0:
  st.write("not valid division")
c=a/b
st.write("division of numbers is:", c)
