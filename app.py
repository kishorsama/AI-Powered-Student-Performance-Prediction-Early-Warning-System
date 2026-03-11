import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("student_model.pkl", "rb"))

st.title("AI Student Performance Prediction System")

st.write("Enter student details")

# Direct numeric input fields
study = st.number_input("Study Time (hours/day)", min_value=0, max_value=10, value=2)

absences = st.number_input("Number of Absences", min_value=0, max_value=30, value=3)

previous = st.number_input("Previous Grade", min_value=0, max_value=100, value=60)

assignments = st.number_input("Assignments Completed", min_value=0, max_value=10, value=5)

participation = st.number_input("Participation Level (1-5)", min_value=1, max_value=5, value=3)


# Prepare input data
input_data = pd.DataFrame({
    "StudyTime":[study],
    "Absences":[absences],
    "PreviousGrade":[previous],
    "AssignmentsCompleted":[assignments],
    "Participation":[participation]
})

# Prediction button
if st.button("Predict Performance"):

    prediction = model.predict(input_data)[0]

    st.subheader(f"Predicted Final Grade: {prediction:.2f}")

    # Classification
    if prediction < 50:
        category = "At Risk"
    elif prediction < 75:
        category = "Average"
    else:
        category = "High Performer"

    st.subheader(f"Performance Category: {category}")

    # Recommendations
    st.write("### Recommendations")

    if study < 2:
        st.write("Increase study time")

    if absences > 7:
        st.write("Improve attendance")

    if participation < 3:
        st.write("Participate more in class")

    if study >=3 and absences <5:
        st.write("Good learning behavior, keep it up!")