
# Network:1
# Import Libraries
import streamlit as st
import json
from streamlit_lottie import st_lottie

# Network:2(a)
# Make column at Header
image_column, text_column = st.columns((1,5))

# Heart Animation
with image_column:
    with open("Animation.json") as source:
        animation=json.load(source)

        st.lottie (animation,height=125,width=100)

with text_column:
    # Network:2(b)
    # Header is given
    st.title("Hospital Management System")
    st.write('Expert in Medical Services:heartbeat:')

# Network:3(a)
# Navigation bar on top
# Function definitions for different pages
def render_home():
    st.subheader("Welcome to the Home Page!")

def render_about():
    st.subheader("Learn more about us here.")

def render_contact():
    st.subheader("Contact us!")

def render_patient():
    st.subheader("Enter your information for record.")

# Initialize session state variables for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define a function to handle navigation
def navigate(page):
    st.session_state.page = page


# Layout for the top navigation bar using columns
col1, col2, col3, col4 = st.columns(4)

# Network:4
# Divider b/w header & body
# Simple HTML to create a colored line
rainbow_html = """
<div style='height: 3px; background: linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(255,154,0,1) 10%, rgba(208,222,33,1) 20%, rgba(79,220,74,1) 30%, rgba(63,218,216,1) 40%, rgba(47,201,226,1) 50%, rgba(28,127,238,1) 60%, rgba(95,21,242,1) 70%, rgba(186,12,248,1) 80%, rgba(251,7,217,1) 90%, rgba(255,0,0,1) 100%);'>
</div>
"""
st.markdown(rainbow_html, unsafe_allow_html=True)
#Network:3(b)
with col1:
    # Use the button's "on_click" to change the page state
    if st.button("Home"):
        navigate('home')

with col2:
    if st.button("About Us"):
        navigate('about')

with col3:
    if st.button("Contact Us"):
        navigate('contact')

with col4:
    if st.button("Patient"):
        navigate('patient')


# Conditional rendering based on the current page
if st.session_state.page == 'home':
    render_home()
    # Network:5
    # image example
    import streamlit as st
    from PIL import Image

    # Load image
    image = Image.open("hms.jpg")

    # Display image
    st.image(image, use_column_width=True)
    
    # Summary about (HMS)
    st.write("The hospital management system (HMS) is an integrated software that handles different directions of clinic workflows. It manages the smooth healthcare performance along with administrative, medical, legal and financial control.")
    st.write("Some basic hospital management system modules are following:")
    
    # Columns for bullet point.
    col1,col2=st.columns(2)

    with col1:
        st.markdown('''
                    - Appointment
                    - Patient Management
                    ''')
    with col2:
        st.markdown('''
                    - Accounts Management
                    - Pharmacy Management
                    ''')
        
    # Bullet Detail.    
    st.subheader("Appointment")
    st.write("Appointment module in hospital management arranges the schedule of doctors due to the patients’ application. It helps to organize the availability of medical specialists at any convenient time. Some hospital can even offer remote visits when you need immediate assistance.")    
    
    st.subheader("Patient Management")
    st.write("It is used to control patient flow. It can be used to register them, get the data of the patients’ health condition, view the treatment and check the medical history and reports.")

    st.subheader("Accounts Management")
    st.write("Accounting module organizes the financial affairs of both customers and the medical institution. It stores and presents all the patient payment details, hospital financial records on expenses and overall profit.")    

    st.subheader("Pharmacy Management")
    st.write("Pharmacy management module contains the list of drugs that usually used for the specific treatment. It keeps records of every patient’ drugs used during their treatment.")            

elif st.session_state.page == 'about':
    render_about()
    text_column, image_column = st.columns((2,1))
    
    with text_column:
        st.write("As'salam-o-Alaikum!")
        st.write('''
             We are the student of Bano Qabil 2.0 and we are donig "Office wizard to Python programming" course from here.
             Our instructor name is GHUFRAN KAMALUDDIN.
             We have created a Hospital Management System project.
             ''')
        # line space
        st.write("###")
        
        st.markdown('''
                    - Project Leader: Farasat-ul-islam
                    - 2nd Member: Syed abdul basit
                    - 3rd Member: Ubaid
                    ''')
    
    # Bano Qabil logo    
    with image_column:
        from PIL import Image
        
        bano = Image.open("Bano Qabil.jpg")
        st.image(bano)

elif st.session_state.page == 'contact':
    render_contact()
    image_column, text_column = st.columns((1,4))
    # Email logo
    with image_column:
        from PIL import Image

        Email= Image.open("E-mail.jpg")
        st.image(Email)

    with text_column:
        st.write("For Technical queries contact us via email at abc@example.com")

    # Divider line
    st.write("---")

    image_column, text_column = st.columns((1,2))
    with image_column:
        from PIL import Image

        Phone= Image.open("Phone.jpg")
        st.image(Phone)

    with text_column:
        st.write("To contact us our team member: 09871234567")




elif st.session_state.page == 'patient':
    render_patient()
# Network:6
    # Patients entry
    
    import sqlite3

    # Create a connection to the SQLite database
    conn = sqlite3.connect('hospital.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table for storing patient details
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        gender TEXT,
                        condition TEXT,
                        address TEXT
                    )''')


    # Function to add a new patient
    def add_patient(name, age, gender, condition, address):
        cursor.execute('''INSERT INTO patients (name, age, gender, condition, address) 
                        VALUES (?, ?, ?, ?, ?)''', (name, age, gender, condition, address))
        conn.commit()
        st.success("Patient added successfully.")

    # Function to remove a patient by ID
    def remove_patient(patient_id):
        cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
        conn.commit()
        st.success("Patient removed successfully.")

    # Function to fetch all patients
    def get_all_patients():
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        for patient in patients:
            st.write(patient)

    # Streamlit UI
    st.header("Patient Entry.")

    # Input fields for adding a new patient
    name = st.text_input("Enter patient's name:")
    age = st.number_input("Enter patient's age:")
    gender = st.selectbox("Select patient's gender:", ['Male', 'Female', 'Other'])
    condition = st.text_input("Enter your condition:")
    address = st.text_area("Enter patient's address:")

    # Button to add patient
    if st.button("Add Patient"):
        add_patient(name, age, gender, condition, address)

    # Button to remove patient
    remove_id = st.number_input("Enter ID of patient to remove:")
    if st.button("Remove Patient"):
        remove_patient(remove_id)

    # Button to view all patients
    if st.button("View All Patients"):
        get_all_patients()

    # Close the cursor and connection
    cursor.close()
    conn.close()





