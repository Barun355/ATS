import streamlit as st
from database import Database

ats_database = Database()

def donateHandle(name, email, amount, upi, transaction_id):    
    unique_code = ats_database.add_proof(name, email, amount, upi, transaction_id)
    
    if unique_code["error"]:
        st.write(unique_code["error"])
        return False
    elif unique_code["unique_code"]:
        st.header("Your unique ID please keep it with you")
        st.write(unique_code["unique_code"])
        return True


def main():
        
    st.header("Help us to improve our service by donating")
    st.image("QR.jpeg", width=400)
    
    with st.form("donate_form"):
        st.header("Thank u For your Kindness")
        donater_name = st.text_input("Enter your name")
        donater_email = st.text_input("Enter your email")
        donater_amount = st.text_input("Amount you donate")
        donater_upi_id = st.text_input("Enter your UPI id")
        transaction_id = st.text_input("Transaction ID")
        donated_button = st.form_submit_button("Donate")
        
    
    if donated_button:
        donateHandle(donater_name, donater_email, donater_amount, donater_upi_id, transaction_id)

main()