import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Patient Upload",
    page_icon="📂",
    layout="wide"
)


st.title("📂 Patient Data Upload")

st.write(
"""
Upload patient information and cognitive data
for AI-based analysis.
"""
)


st.divider()


# Patient Information

st.subheader("Patient Information")


col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Patient Name"
    )


    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )


with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )


st.divider()


# File Upload

st.subheader("Upload Cognitive Data")


uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


if uploaded_file:

    data = pd.read_csv(uploaded_file)

    st.success(
        "File uploaded successfully!"
    )


    st.subheader("Dataset Preview")

    st.dataframe(data)


st.divider()


if st.button("🔍 Analyze Data"):

    st.success(
        "Analysis started..."
    )

    st.info(
        "Connecting with SNN model..."
    )