import streamlit as st
from Feature_01 import return_even,return_odd
import time

original_list = [i for i in range (10)]

with st.spinner('Computing even and odd lists...'):
    # simulate work (optional)
    time.sleep(5)
    even_list = return_even(original_list)
    odd_list = return_odd(original_list)
    st.success('Computed lists')

st.write('hooray, we made it')

st.write('Hello, world')

st.write(even_list)

st.write(odd_list)

def addition(a,b):
    return a + b
A=2
B=3

with st.spinner('Calculating addition...'):
    time.sleep(0.2)
    result = addition(A,B)
    st.success('Done')

st.write(result)