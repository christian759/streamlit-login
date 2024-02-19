import streamlit as st
import streamlit_authenticator as stauth
from pages import page1
import time

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'By CEO1'; 
                visibility: visible;
                display: block;
                position: relative;
                background-color: red;
                padding: 5px;
                top: 2px;
}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Page for login
if not hasattr(st.session_state, 'username') or st.session_state.username is None:
    st.header('Login')

# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if 'oklogin' not in st.session_state:
    # This is our variable.
    st.session_state.oklogin = False

if email == actual_email and password == actual_password:
    st.session_state.oklogin = True
    checker = True

if st.session_state.oklogin:
    # Your content here
    if st.session_state.oklogin:
        placeholder.empty()
        st.success("Login successful")
        st.balloons()
        st.session_state.username = email
        st.session_state.page = page1
                  
    
    else:
        st.error("Invalid credentials. Please try again.")


    
	