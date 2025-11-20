import streamlit as st
import numpy as np

# --------------------------
# Streamlit UI
# --------------------------
st.title("🩸 Smart Glucose Predictor (Demo)")
st.write("Enter your last **12 glucose** readings to predict your next glucose level.")

input_mode = st.radio("Input mode:", ["One by one", "Enter values as comma-separated row"])

if input_mode == "One by one":
    glucose_inputs = []
    # Input fields
    for i in range(12):
        g = st.number_input(f"Glucose {i+1}", min_value=0.0, value=100.0)
        glucose_inputs.append(g)
else:
    glucose_str = st.text_input("Enter 12 glucose readings (comma-separated):", 
                               "100, 105, 98, 110, 99, 102, 101, 104, 100, 103, 98, 100")
    # Convert to list of floats
    try:
        glucose_inputs = [float(x.strip()) for x in glucose_str.split(",")]
        if len(glucose_inputs) != 12:
            st.error("Please enter exactly 12 glucose values.")
            glucose_inputs = None
    except:
        st.error("Invalid input: Please enter numeric comma-separated values.")
        glucose_inputs = None

# --------------------------
# Fake Prediction Logic
# --------------------------
if st.button("Predict Next Glucose Level") and glucose_inputs:
    avg_glucose = np.mean(glucose_inputs)
    predicted_glucose = avg_glucose + np.random.normal(0, 5)  # small random noise

    # Interpret glucose levels (typical ranges)
    if predicted_glucose < 70:
        message = "Your glucose is low. Please consult your healthcare provider."
    elif 70 <= predicted_glucose <= 140:
        message = "Your glucose is normal."
    else:
        message = "Your glucose is high. Please take necessary precautions."

    st.success(f"Predicted Glucose: **{predicted_glucose:.2f} mg/dL**")
    st.info(message)
