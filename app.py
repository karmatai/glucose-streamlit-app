import streamlit as st
import numpy as np

# --------------------------
# Streamlit UI
# --------------------------
st.title("🩸 Smart LSTM Glucose Predictor (Demo)")
st.write("Enter your last **12 glucose** and **12 insulin** readings to predict your next glucose level.")

cols = st.columns(2)
glucose_inputs = []
insulin_inputs = []

# Input fields
for i in range(12):
    with cols[0]:
        g = st.number_input(f"Glucose {i+1}", min_value=0.0, value=100.0)
    with cols[1]:
        ins = st.number_input(f"Insulin {i+1}", min_value=0.0, value=10.0)

    glucose_inputs.append(g)
    insulin_inputs.append(ins)

# --------------------------
# Fake Prediction Logic
# --------------------------
if st.button("Predict Next Glucose Level"):
    # Just simulate a prediction by taking the average glucose and adding some noise
    avg_glucose = np.mean(glucose_inputs)
    predicted_glucose = avg_glucose + np.random.normal(0, 5)  # small random noise

    st.success(f"Predicted Glucose: **{predicted_glucose:.2f} mg/dL**")
