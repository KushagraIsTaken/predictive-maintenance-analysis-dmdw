# Import Required Libraries
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
import joblib

# Load the saved model
model = joblib.load('random_forest_model.pkl')

# Streamlit app title
st.title("Machine Learning Prediction App")

# Sidebar for project information
st.sidebar.header("Project Information")
st.sidebar.subheader("Predictive Maintenance Analytics")
st.sidebar.text("Submitted to: Dr. Mukesh Kumar")
st.sidebar.text("Data Mining & Data Warehousing Course")
st.sidebar.text("Submitted by: Kushagra Agrawal")
st.sidebar.text("Date: October 2024")
st.sidebar.text("Contact Information: kush4409@gmail.com")

# Input fields for features
st.subheader("Enter Input Features for Prediction")

# Input fields for required features
air_temperature = st.number_input("Air Temperature (°C)", value=0.0)
process_temperature = st.number_input("Process Temperature (°C)", value=0.0)
rotational_speed = st.number_input("Rotational Speed (rpm)", value=0.0)
torque = st.number_input("Torque (Nm)", value=0.0)
tool_wear = st.number_input("Tool Wear (mins)", value=0.0)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'Air_temperature': [air_temperature],
    'Process_temperature': [process_temperature],
    'Rotational_speed': [rotational_speed],
    'Torque': [torque],
    'Tool_wear': [tool_wear]
})

# Prediction button
if st.button("Predict"):
    # Display the input values
    st.write("Input values for prediction:")
    st.write(input_data)

    # Make predictions
    predictions = model.predict(input_data)
    
    # Create a DataFrame for the predictions
    predictions_df = pd.DataFrame(predictions, columns=['Machine_failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'])
    
    # Display predictions
    st.subheader("Predictions")
    st.write(predictions_df)

    # Final statement based on machine failure prediction
    if predictions_df['Machine_failure'][0] == 0:
        st.success("The machine will **not fail**.")
    else:
        st.error("The machine will **fail** with the following reason(s):")
        reasons = []
        if predictions_df['TWF'][0] == 1:
            reasons.append("Tool Wear Failure (TWF): The tool will be replaced or fail at a randomly selected tool wear time between 200 – 240 mins.")
        if predictions_df['HDF'][0] == 1:
            reasons.append("Heat Dissipation Failure (HDF): Causes a process failure if the difference between air and process temperature is below 8.6 K and the tool’s rotational speed is below 1380 rpm.")
        if predictions_df['PWF'][0] == 1:
            reasons.append("Power Failure (PWF): The product of torque and rotational speed is outside the required range.")
        if predictions_df['OSF'][0] == 1:
            reasons.append("Overstrain Failure (OSF): The product of tool wear and torque exceeds the threshold for failure.")
        if predictions_df['RNF'][0] == 1:
            reasons.append("Random Failure (RNF): There is a 0.1% chance of failure regardless of process parameters.")
        
        # Display reasons
        for reason in reasons:
            st.write(f"- {reason}")

