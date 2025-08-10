
import streamlit as st
import pickle
import numpy as np

# Load the trained model
# Make sure 'model.pkl' exists in the same directory when deploying
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Heart Stroke Prediction", page_icon="❤️", layout="centered")

st.title("❤️ Heart Stroke Prediction App")
st.write("Enter patient details to check the risk of heart stroke.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", [0, 1])
cp = st.number_input("cp", min_value=0, max_value=3, value=3)
trestbps = st.number_input("trestbps", min_value=0.0, max_value=300.0, value=140.0)
chol = st.number_input("chol", min_value=0.0, max_value=500.0, value=250.0)
fbs = st.selectbox("fbs", [0, 1])
restecg = st.selectbox("restecg", [0, 1])
thalach = st.number_input("thalach", min_value=0, max_value=200)
exang = st.selectbox("exang", [0, 1])
oldpeak = st.number_input("oldpeak", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("slope", [0, 1, 2])
ca = st.number_input("ca", min_value=0, max_value=4, value=0)
thal = st.selectbox("thal", [1, 2, 3])


# Encoding categorical inputs (adjust as per your training preprocessing)
gender_map = {"Male": 1, "Female": 0, "Other": 2}
smoking_map = {"never smoked": 0, "formerly smoked": 1, "smokes": 2, "Unknown": 3}

if st.button("Predict"):
    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])
    
    prediction = model.predict(input_data)
    result = "🚨 High Risk of Stroke" if prediction[0] == 1 else "✅ Low Risk of Stroke"
    
    st.subheader("Prediction Result")
    if prediction[0] == 0:
        st.success(result)
    else:
        st.error(result)

st.markdown("---")
st.caption("Machine Learning model for educational purposes. Not for medical use.")
