import streamlit as st
from Feature_01 import return_even

original_list = [i for i in range (10)]

even_list = return_even(original_list)

new_list = [i for i in range (10)]

odd_list = return_odd(new_list)

st.write('hooray, we made it')

st.write('Hello, world')

st.write(even_list)

def addition(a,b):
    return a + b
A=2
B=3

st.write(addition(A,B))