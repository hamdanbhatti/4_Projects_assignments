import streamlit as st

# Title
st.title("🧮 BMI Calculator")

# User inputs
st.write("Enter your details below:")

weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (cm)", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        # BMI formula: weight (kg) / (height (m)^2)
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        st.subheader(f"Your BMI is: {bmi}")

        # Categories
        if bmi < 18.5:
            st.warning("You are Underweight 😕")
        elif 18.5 <= bmi < 24.9:
            st.success("You have Normal weight 🙂")
        elif 25 <= bmi < 29.9:
            st.warning("You are Overweight 😐")
        else:
            st.error("You are Obese 😟")
    else:
        st.error("Please enter valid values.")
