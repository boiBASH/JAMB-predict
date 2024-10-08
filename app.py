import streamlit as st
import joblib
import pandas as pd

# Cache the model using st.cache_resource
@st.cache_resource
def load_model():
    return joblib.load('random_forest_jamb_model.pkl')

model = load_model()  # Load the model only once

# Sidebar information and navigation
st.sidebar.title("JAMB Score Prediction App")
st.sidebar.info("""
Use this app to predict a student's JAMB score based on their grades across multiple subjects. 
Select the appropriate grades and department, and hit the "Predict JAMB Score" button.
""")

# Main page title and header
st.markdown("""
    <style>
        .stTitle {
            color: #FF6347;  /* Tomato red */
            font-family: 'Helvetica';
            text-align: center;
        }
        .stHeader {
            color: #4CAF50;  /* Green */
            text-align: left;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 JAMB Score Prediction")
st.markdown("""
### Enter Student's Grades
Provide the grades for the following subjects and select the department.
""")

# List of subjects
subjects = ['Biology', 'Chemistry', 'Civic Education', 'Commerce',
            'Economics', 'English', 'Further Mathematics',
            'Government', 'Geography', 'Literature in English',
            'Mathematics', 'Physics']

# Create a dictionary to store subject grades
grades = {}

# Create selectboxes for each subject grade
for subject in subjects:
    grades[subject] = st.selectbox(f"{subject} Grade", 
                                   options=['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9', 'ABS'], 
                                   index=9)

# Selectbox for Department
department = st.selectbox("Department", ['Arts', 'Science', 'Commercial'])

# Convert the input into a DataFrame
input_data = pd.DataFrame([grades])
input_data['Department'] = department

# Map grades to numerical values
grade_mapping = {
    'A1': 6, 'B2': 5, 'B3': 4, 'C4': 3, 'C5': 2, 'C6': 1,
    'D7': 0, 'E8': 0, 'F9': 0, 'ABS': None  # Use None for absent scores
}

# Apply the grade mapping to the input data
for col in subjects:
    input_data[col] = input_data[col].map(grade_mapping)

# Handle ABS by replacing None with a default value (0 for instance)
input_data = input_data.fillna(0)

# Ensure all required columns are present, filling missing columns with zeros
required_columns = subjects + ['Department']  # Model expects all these columns
for col in required_columns:
    if col not in input_data.columns:
        input_data[col] = 0  # Default value for missing columns

# Button to trigger the prediction
if st.button('Predict JAMB Score'):
    # Ensure that there are still enough subjects after removing ABS
    if input_data.shape[1] < 2:  # Assuming we need at least 2 subjects to predict
        st.error("Please provide valid grades for at least two subjects to make a prediction.")
    else:
        # Make a prediction
        prediction = model.predict(input_data)[0]
        # Display the prediction result
        st.success(f"🎯 Predicted JAMB Score: {prediction:.2f}")

        # Provide downloadable result
        csv = input_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Prediction",
            data=csv,
            file_name='jamb_prediction.csv',
            mime='text/csv'
        )

# Footer
st.markdown("""
---
#### **JAMB Prediction App**  
Built by [boiBASH](https://yourportfolio.com)  
Contact: [Bashirudeenopeyemi772@gmail.com](mailto:your.email@example.com)
""")
