import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# --------------------------
# Load Model + Scaler (cached)
# --------------------------
@st.cache_resource
def load_ai():
    model = load_model("lstm_realdata_model_fixed.h5", compile=False)
    scaler = joblib.load("scaler.save")
    return model, scaler


# --------------------------
# Streamlit UI
# --------------------------
st.title("🩸 Smart LSTM Glucose Predictor")
st.write("Enter your last **12 glucose** and **12 insulin** readings to predict your next glucose level.")

cols = st.columns(2)
glucose_inputs = []
insulin_inputs = []

# Input fields
for i in range(12):
    with cols[0]:
        g = st.number_input(f"Glucose {i+1}", min_value=0.0, value=0.0)
    with cols[1]:
        ins = st.number_input(f"Insulin {i+1}", min_value=0.0, value=0.0)

    glucose_inputs.append(g)
    insulin_inputs.append(ins)

# --------------------------
# Prediction Logic
# --------------------------
if st.button("Predict Next Glucose Level"):
    # Prepare input array
    data = np.array(list(zip(glucose_inputs, insulin_inputs)))

    # Scale
    data_scaled = scaler.transform(data)
    data_scaled = np.expand_dims(data_scaled, axis=0)

    # Predict
    pred_scaled = model.predict(data_scaled)

    # Inverse scale
    pred_value = scaler.inverse_transform(
        np.concatenate([pred_scaled, np.zeros((1,1))], axis=1)
    )[:, 0]

    st.success(f"Predicted Glucose: **{pred_value[0]:.2f} mg/dL**")
