import streamlit as st
from database import Database

ats_database = Database()


with st.form("donate_form", clear_on_submit=True):
    st.header("Enter your Details")
    name = st.text_input("Write your Name")
    email = st.text_input("Write your Email")
    phone_number = st.text_input("Write your Phone Number")
    address = st.text_area("Write your Address")
    education = st.text_area("Write your Education")
    about_me = st.text_area("Write some points about yourself")
    experience = st.text_area("Write your Experience (in points)")
    projects = st.text_area("Write your Projects (in points)")
    soft_skills = st.text_area("Write your Soft Skills (seperated by comma)")
    linkedin_link = st.text_area("Give your LinkedIn Profile link")
    social_media_link = st.text_area("Give your Social Media profile links")
    skills = st.text_area("Write your Techanical Skills (For your domain)")
    job_description = st.text_area("Give the Job description you are applying for")
    hard_copy = st.checkbox("You want physical copy of your resume! Yes/No", False)
    submit = st.form_submit_button("Generate")

if submit:
    if job_description == "":
        st.error("Name, Email, Phone Number, Address, Education and Job Description is compulsory")
        st.focus(name)
        st.focus(email)
        st.focus(phone_number)
        st.focus(education)
        st.focus(job_description)
        st.stop()
    
    if hard_copy:
        st.write("currently we not provide hard service")
        
    detail = ats_database.create_resume(name=name, email=email, phone_number=phone_number, address=address, education=education, about_me=about_me, experience=experience, projects=projects, soft_skills=soft_skills, linkedin_link=linkedin_link, social_media_link=social_media_link, skills=skills, job_description=job_description)
    
    if detail["status"]:
        st.write("Resume submited, we will get to you soon")
    else:
        st.write("Somer Error Occured")