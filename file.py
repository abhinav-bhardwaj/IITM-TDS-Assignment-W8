import streamlit as st
st.title("Streamlit Application to add two numbers")
st.write("Roll No. - 21F1001318")
st.write("IITM TDS May2022 Term Week 8 Assignment")
Fno = st.number_input("Enter first no. : ")
Sno = st.number_input("Enter second no. : ")
summ = Fno+Sno
st.write("Addition of given numbers : ",summ)
