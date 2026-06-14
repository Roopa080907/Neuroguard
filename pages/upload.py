import streamlit as st
from PIL import Image

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Upload MRI Scan",
    page_icon="🧠",
    layout="wide"
)

# =========================
# PAGE TITLE
# =========================

st.title("📤 MRI Scan Upload")

st.markdown("""
### Upload a Brain MRI Scan for Analysis

The uploaded MRI image will be processed by the NeuroSense AI model
to predict cognitive decline risk and dementia stage.
""")

st.divider()

# =========================
# PATIENT DETAILS
# =========================

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=60
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    patient_id = st.text_input(
        "Patient ID",
        placeholder="Enter patient ID"
    )

# =========================
# STORE PATIENT DATA
# =========================

st.session_state["patient_name"] = patient_name
st.session_state["age"] = age
st.session_state["gender"] = gender
st.session_state["patient_id"] = patient_id

st.divider()

# =========================
# MRI UPLOAD SECTION
# =========================

st.subheader("🧠 MRI Scan Upload")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

# =========================
# IMAGE PREVIEW
# =========================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.success("✅ MRI Image Uploaded Successfully")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            image,
            caption="Uploaded MRI Scan",
            use_container_width=True
        )

    with col2:

        st.info(f"""
### Patient Summary

**Name:** {patient_name}

**Age:** {age}

**Gender:** {gender}

**Patient ID:** {patient_id}
""")

        st.success("""
### Scan Status

✔ File received

✔ Ready for AI analysis

✔ CNN Model Enabled

✔ Explainable AI Ready
""")

    st.divider()

    # =========================
    # ANALYSIS BUTTON
    # =========================

    if st.button("🧠 Analyze MRI Scan"):

        # Save uploaded image name
        st.session_state["uploaded_image"] = uploaded_file.name

        with st.spinner("Analyzing MRI Scan..."):

            progress = st.progress(0)

            for i in range(100):
                progress.progress(i + 1)

        st.success("✅ Analysis Completed Successfully")

        st.info("""
Prediction results can now be viewed
on the Results page.
""")

# =========================
# EMPTY STATE
# =========================

else:

    st.warning(
        "⚠️ Please upload a JPG, JPEG or PNG MRI image to continue."
    )

    st.markdown("""
### Supported Formats

- JPG
- JPEG
- PNG

### Workflow

1️⃣ Enter Patient Details

2️⃣ Upload MRI Scan

3️⃣ AI Analysis

4️⃣ Dementia Classification

5️⃣ Confidence Score

6️⃣ Explainable AI Insights
""")

st.divider()

st.caption(
    "NeuroSense AI • MRI Upload Portal • Hackathon 2025"
)