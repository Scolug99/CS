import streamlit as st
from Feature_01 import return_even,return_odd

original_list = [i for i in range (10)]

even_list = return_even(original_list)

odd_list = return_odd(original_list)

st.write('hooray, we made it')

st.write('Hello, world')

st.write(even_list)

st.write(odd_list)

def addition(a,b):
    return a + b
A=2
B=3

st.write(addition(A,B))