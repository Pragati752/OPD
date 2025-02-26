import smtplib
import random
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from key import password

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "pragatimusale257@gmail.com"
EMAIL_PASSWORD = password

def send_otp(email):
    otp = str(random.randint(100000, 999999))
    st.session_state["otp"] = otp

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = email
    msg["Subject"] = "Your OTP Code"
    msg.attach(MIMEText(f"Your OTP code is {otp}", "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error("Failed to send OTP. Check your email settings.")
        return False

def verify_otp(user_input_otp):
    return user_input_otp == st.session_state.get("otp")