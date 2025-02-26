import streamlit as st
from otp import send_otp,verify_otp
from OPD import main

st.title("OPD BOOKING Chatbot")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.subheader("Email OTP Verification")

    email = st.text_input("Enter your email")
    if st.button("Send OTP"):
        if send_otp(email):
            st.success("OTP sent successfully!")
            
    otp_input = st.text_input("Enter OTP")
    if st.button("Verify OTP"):
        if verify_otp(otp_input):
            st.success("Verified!")
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid OTP!")

if st.session_state["authenticated"]:
   st.subheader("Chat with our AI Bot!")
   response = main()
        