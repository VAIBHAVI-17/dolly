import streamlit as st
st.title("TDS Week 8 Module")
a=st.number_input("Enter first number")
b=st.number_input("Enter second number", value=1)
try:
  c=a/b
except ZeroDivisionError:
  st.write("Dic=vision by zero is not posible")
else:
  st.write("Division answer is",c)
