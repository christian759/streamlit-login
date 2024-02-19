import streamlit as st

if 'oklogin' not in st.session_state:
    st.session_state.oklogin = False

if st.session_state.oklogin:
    st.info('Home Page')
    st.balloons()
else:
    st.error('Please log in in the main page.')