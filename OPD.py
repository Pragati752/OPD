import streamlit as st
import datetime
import numpy as np
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from key import password

EMAIL_ADDRESS = "pragatimusale257@gmail.com"
EMAIL_PASSWORD = password

def send_email(to_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def main():
    st.title("OPD Booking Chatbot")
    st.subheader("Book your doctor appointments quickly and easily!")

    st.write("Hi! I'm your OPD Booking Assistant. Let's schedule your appointment.")

    email = st.text_input("Enter your email for confirmation:")

    departments = np.array(["General Medicine", "Cardiology", "Orthopedics", "Gynecology", "Dermatology", "ENT", "Pediatrics", "Opthamology", "Radiology", "Neurology", "Psychiatry", "Oncology", "Pathology", "Nephrology"])
    department = st.selectbox("Choose the department you want to book an appointment with:", departments)

    doctor_options = {
        "General Medicine": ["Dr. Rajesh Kumar", "Dr. Sneha Patel", "Dr. Devansh Rawat"],
        "Cardiology": ["Dr. Anil Mehta", "Dr. Priya Sharma", "Dr. Ira Bhandari"],
        "Orthopedics": ["Dr. Manoj Desai", "Dr. Akash Gupta", "Dr. Aditi Saini"],
        "Gynecology": ["Dr. Neeta Verma", "Dr. Riya Nair", "Dr. Nirav Bafna"],
        "Dermatology": ["Dr. Ramesh Rao", "Dr. Kritika Singh", "Dr. Vedika Gokhale"],
        "ENT": ["Dr. Kavita Shah", "Dr. Arun Malhotra", "Dr. Tanmay Godbole"],
        "Pediatrics": ["Dr. Meera Iyer", "Dr. Anuj Roy", "Dr. Shravani Jagtap"],
        "Opthamology": ["Dr. Shlok Gupta", "Dr. Anirudh Bose", "Dr. Meghna Barua"],
        "Radiology": ["Dr. Shweta Arora", "Dr. Alex Lima", "Dr. Nishant Achar"],
        "Neurology": ["Dr. Prerana Musale", "Dr. Rishank Rai", "Dr. Trishita Senapati"],
        "Psychiatry": ["Dr. Dev Bhalla", "Dr. Ellsy Perrie", "Dr. Kabir Bhasin"],
        "Oncology": ["Dr. Sharvari Bhosale", "Dr. Krisha Mathur", "Dr. Tanishq Vaid"],
        "Pathology": ["Dr. Jhanvi Sen", "Dr. Rohan Pratap", "Dr. Tanvika Madhavan"],
        "Nephrology": ["Dr. Eesha Krishna", "Dr. Siya Thakur", "Dr. Devika Lele"]
    }

    doctor = st.selectbox("Select a doctor:", doctor_options[department])

    appointment_date = st.date_input("Select an appointment date:", min_value=datetime.date.today())

    time_slots = np.array(["9:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "2:00 PM - 3:00 PM", "3:00 PM - 4:00 PM", "4:00 PM - 5:00 PM"])
    time_slot = st.selectbox("Choose a preferred time slot:", time_slots)

    patient_name = st.text_input("Enter your name:")
    patient_age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    gender_options={'Male','Female','Other'}
    patient_gender=st.selectbox("Enter your gender:",gender_options)
    contact_number = st.text_input("Enter your contact number:")
    patient_city = st.text_input("Enter your city:")

    if st.button("Confirm Appointment"):
        if patient_name and contact_number and email:
            appointment_details = (f"Appointment successfully booked!\n\nDepartment:{department}\nDoctor:{doctor}\n"
                                   f"Date:{appointment_date}\nTime:{time_slot}\nPatient Name:{patient_name}\nGender:{patient_gender}\n"
                                   f"Age:{patient_age}\nContact:{contact_number}\nCity:{patient_city}")
            st.success(appointment_details)
            send_email(email, "Appointment Confirmation", appointment_details)
            

            appointment_data = pd.DataFrame({
                "Department": [department],
                "Doctor": [doctor],
                "Date": [appointment_date],
                "Time Slot": [time_slot],
                "Patient Name": [patient_name],
                "Gender":[patient_gender],
                "Age": [patient_age],
                "Contact": [contact_number],
                "City": [patient_city]
            })
            st.dataframe(appointment_data)
            st.info("A confirmation email has been sent to your email address.")
        else:
            st.error("Please enter all required details to confirm your appointment.")

if __name__ == "__main__":
    main()
