import streamlit as st
import joblib
import pandas as pd
from streamlit_option_menu import option_menu
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
import base64
# Load the trained model
model = joblib.load('loan_approval_model.pkl')

# Define the function to make predictions
def predict_loan_approval(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app
st.title("Loan Approval Prediction System")

# Input fields for user data
st.sidebar.header("Menu")
if __name__ == '__main__':
    st.markdown("## Loan Approval Prediction System")
    with st.sidebar:
        selected = option_menu('Loan Approval Prediction System',
                          ['Predict Loan Approval',
                           'Our Prediction Records',
                           'About Me'],
                          icons=['info','book','info'],
                          default_index=0)

if selected =="Predict Loan Approval":
    # Example input fields
    Name = st.text_input('Enter your name:')
    gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    married = st.selectbox("Married", options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    education = st.selectbox("Education", options=[0, 1], format_func=lambda x: 'Graduate' if x == 1 else 'Not Graduate')
    self_employed = st.selectbox("Self Employed", options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    applicant_income = st.number_input("Applicant Income", min_value=0, value=50000)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)
    loan_amount = st.number_input("Loan Amount", min_value=0.0, value=10000.0)
    loan_amount_term = st.number_input("Loan Amount Term", min_value=0.0, value=360.0)
    credit_history = st.selectbox("Credit History", options=[0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
    property_area = st.selectbox("Property Area", options=[0, 1, 2], format_func=lambda x: ['Urban', 'Semiurban', 'Rural'][x])
    dependents = st.number_input("Dependents", min_value=0, value=0)

    # Collect inputs into a list
    user_input = [gender, married, education, self_employed, applicant_income, coapplicant_income,
              loan_amount, loan_amount_term, credit_history, property_area, dependents]
    
# Predict
    if st.button("Predict"):
        result = predict_loan_approval(user_input)
        if result == 1:
            st.success("Loan Approved")
        else:
            st.error("Loan Denied")
        f = open("user_records.txt", "a")
            f.write("\n")
            new_data = str([Name, gender, married, education, self_employed, applicant_income, coapplicant_income,
              loan_amount, loan_amount_term, credit_history, property_area, dependents, result])
            leng = len(new_data)
            f.write(new_data[1:leng-1]) 
            f.close()
        
    def generate_report(Name, result):
                buffer = BytesIO()
                c = canvas.Canvas(buffer, pagesize=letter)
                width, height = letter
                c.drawString(100, height-50, "Loan Prediction Report")
                c.drawString(100, height-70, "--------------------------------------------")
                c.drawString(100, height-90, f"Name: {Name}")
                c.drawString(100, height-110, f"Gender: {gender}")
                c.drawString(100, height-130, f"Married?: {married}")
                c.drawString(100, height-150, f"education Status: {education}")
                c.drawString(100, height-170, f"Self Employed?): {self_employed}")
                c.drawString(100, height-190, f"Income: {applicant_income}")
                c.drawString(100, height-210, f"Gurrantor Income: {coapplicant_income}")
                c.drawString(100, height-230, f"Loan Amount: {loan_amount}")
                c.drawString(100, height-250, f"Credit History: {credit_history}")
                c.drawString(100, height-270, f"Property: {property_area}")
                c.drawString(100, height-290, f"Dependents: {dependents}")
                c.drawString(100, height-310, "--------------------------------------------")
                c.drawString(100, height-330, "Prediction:")
                if result == 1:
                   c.setFillColorRGB(1, 0, 0)  # Red color
                   prediction_text = "Loan Approved"
                else:
                   c.setFillColorRGB(0, 1, 0)  # Green color
                   prediction_text = "Loan Not Approved"
                c.drawString(100, height-340, f"{prediction_text}")
                c.setFillColor(colors.black)
                c.setFont("Helvetica", 10)
                footnote = "Note: The prediction is based on probability. Actual results may vary. Please consult an expert for a detailed check."
                c.drawString(100, 200, footnote)
                c.showPage()
                c.save()
                pdf_bytes = buffer.getvalue()
                buffer.close()
                return pdf_bytes
               
    pdf_bytes = generate_report(Name, result)
    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<a href="data:application/pdf;base64,{pdf_base64}" download="diabetes_report_{Name}.pdf">Download Report</a>'
    st.markdown(pdf_display, unsafe_allow_html=True)
           
if selected == "Our Prediction Records":
        st.markdown("<h3 style='text-align: center;'>PREDICTION RECORDS OF OUR PREVIOUS USERS</h1>", unsafe_allow_html=True)
        f = pd.read_csv("user_records.txt")
        #st.table(f)
        st.table(f.style.set_table_attributes('style="width:100%;"'))
        st.markdown("____")
        st.write("All the records are stored only for academic and research purpose & will not be used for any other means.")
        
    if selected == "About Me":
        st.markdown("<h2 style='text-align: center;'>ABOUT</h2>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'>This is an academic project made by B.Tech Computer Science And Engineering 3rd year student.</p>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<h4 style='text-align: center;'>Developed and maintained by</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Subrata Bhuin</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>subratabhuin6@gmail.com</p>", unsafe_allow_html=True)
        st.markdown("____")
