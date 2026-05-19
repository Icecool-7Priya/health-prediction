import streamlit as st

st.title("Disease Prediction System")
st.set_page_config(layout="wide")
st.subheader("Diseases Prediction is an application to predict the various diseases")
st.image("https://tse4.mm.bing.net/th/id/OIP.2Xban2BRxWEcoumeanReigHaEo?pid=Api&P=0&h=180",width=300)

st.subheader("Models:")
st.write("- Diabetes Prediction")
st.write("- Cancer Prediction")
st.write("- Parkinsons Prediction")
st.write("-----")

st.sidebar.title("Navigation")
pageoption =st.sidebar.radio("Navigation",["Home","Diabetes Prediction","Cancer Prediction","Parkinsons Prediction"])

if (pageoption == "Home"):
    st.write("Welcome to the Diseases Prediction system")

elif (pageoption == "Diabetes Prediction"):

    st.subheader("Diabetes Prediction")

    genetic_markers = st.number_input("Genetic Marker", min_value=0, max_value=10, value=0)

    autoantibodies = st.number_input("Autoantibodies", min_value=0, max_value=10, value=0)

    family_History = st.number_input("Family History", min_value=0, max_value=10, value=0)

    insulin_Levels = st.number_input("Insulin Levels", min_value=0, max_value=10, value=0)

    age = st.number_input("Age", min_value=0, max_value=85, value=0)

    bmi = st.number_input("BMI", min_value=0, max_value=100, value=0)

    blood_Pressure = st.number_input("Blood Pressure", min_value=0, max_value=300, value=0)

    cholestrol = st.number_input("Cholesterol Levels", min_value=0, max_value=500, value=0)

    waist_Circumference = st.number_input("Waist Circumference", min_value=0, max_value=200, value=0)

    blood_Glucose_Levels = st.number_input("Blood Glucose Levels", min_value=0, max_value=500, value=0)

    glucose_Tolerance_Test = st.number_input("Glucose Tolerance Test", min_value=0, max_value=10, value=0)

    history_of_PCOS = st.number_input("History of PCOS", min_value=0, max_value=10, value=0)

    previous_gestational_Diabetes = st.number_input(
        "Previous Gestational Diabetes",
        min_value=0,
        max_value=10,
        value=0
    )

    weight_Gain_During_Pregnancy = st.number_input(
        "Weight Gain During Pregnancy",
        min_value=0,
        max_value=100,
        value=0
    )

    pancreatic_Health = st.number_input(
        "Pancreatic Health",
        min_value=0,
        max_value=10,
        value=0
    )

    cystic_Fibrosis_Diagnosis = st.number_input(
        "Cystic Fibrosis Diagnosis",
        min_value=0,
        max_value=10,
        value=0
    )

    steroid_Use_History = st.number_input(
        "Steroid Use History",
        min_value=0,
        max_value=10,
        value=0
    )

    liver_Function_Tests = st.number_input(
        "Liver Function Tests",
        min_value=0,
        max_value=500,
        value=0
    )

    urine_Test = st.number_input(
        "Urine Test",
        min_value=0,
        max_value=10,
        value=0
    )

    birth_Weight = st.number_input(
        "Birth Weight",
        min_value=0,
        max_value=10000,
        value=0
    )

elif (pageoption == "Cancer Prediction"):
    st.subheader("Cancer Prediction")

elif (pageoption == "Parkinsons prediction"):
    st.subheader("Parkinsons prediction")
