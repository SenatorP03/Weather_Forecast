
import streamlit as st
from send_email import send_email

st.header("Contact Me")



with st.form(key="emai_forms"):
    user_email = st.text_input("enter an email address")
    opinion = st.selectbox("Comment", df["topic"])

    raw_message = st.text_area("Your comment here")
    message = (f"""\
Subject:New email from {user_email}

{user_email}
{opinion}
{raw_message}
""")
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Thanks for Sharing")
