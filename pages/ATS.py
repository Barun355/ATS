from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import base64
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(upload_file):
    if upload_file is not None:
        ## Convert pdf to image
        images = pdf2image.convert_from_bytes(upload_file.read())

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() #encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")


## Streamlit App

st.set_page_config(page_title="RF-Automation: ATS Resume Expert")

def ats():
    st.header("Application Tracking System");

    input_text = st.text_area("Job Description: ", key="input")
    uploaded_file = st.file_uploader("Upload Your Resume(PDF)", type=["pdf"])


    if uploaded_file is not None:
        st.write("PDF Uploaded Successfully")

    submit1 = st.button("Tell Me About the Resume")
    # submit2 = st.button("How can I improve my skills")
    submit3 = st.button("Percentage Match")


    input_prompt1 = """
        You are an experienced Technical HR Manager with Tech Experience in the field of any job role from Data Science, Full Stack Web Devlopment, Big Data Engineering, DEVOPS, Data Analyst, your task is to review
        the provided resume against the job description for this profiles.
        Please share your professional evaluation on whether the candidate's profile aligns with the role.
        Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
        If the given resume details doesn't match with the job description then give a guide, how to make the resume specifically for the job dexcription.
    """

    input_prompt3 = """
        You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Devlopment, Big Data Engineering, DEVOPS, Data Analyst, and deep ATS functionality, 
        your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
        the job description. First the output should come as percentage and then keywords missing and last final thoughts.
        if the job description doesn't match the criteria then the percentage should be shown accordingly which can lie from 0 percent to 100 percentage
    """


    if submit1:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.subheader("The Response is: ")
            st.write(response)
        else:
            st.write("Please Upload a pdf")


    elif submit3:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("The Response is: ")
            st.write(response)
        else:
            st.write("Please Upload a pdf")
ats()