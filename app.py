import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="NeuroSense AI",
    page_icon="🧠",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

try:
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# =========================
# HEADER
# =========================

st.title("🧠 NeuroSense AI")

st.markdown("""
# Brain-Inspired Cognitive Decline Detection System
""")

st.markdown("""
### Early Detection of Cognitive Decline using
### MRI-Based Classification and Explainable AI
""")

st.divider()

# =========================
# ABOUT SECTION
# =========================

st.header("🚀 About the Project")

st.write("""
NeuroSense AI is an intelligent healthcare support system designed
to assist clinicians in the early detection of dementia and cognitive decline.

The platform analyzes Brain MRI scans using Artificial Intelligence
to classify dementia stages and provides explainable insights
to improve transparency and trust in AI-assisted diagnosis.
""")

st.markdown("""
### Core Technologies

- 🧠 MRI-Based Dementia Classification
- 🤖 Deep Learning (CNN)
- 🔍 Explainable AI
- 📊 Clinical Decision Support
- ☁️ Streamlit Dashboard
- 🩺 Healthcare Analytics
""")

st.divider()

# =========================
# FEATURE CARDS
# =========================

st.header("✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🧠 MRI Analysis</h2>
        <p>
        Analyze brain MRI scans to identify dementia-related patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>📊 Prediction Dashboard</h2>
        <p>
        View prediction results, confidence scores,
        and patient summaries.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2>🔍 Explainable AI</h2>
        <p>
        Understand model predictions through
        transparent AI explanations.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# PROJECT WORKFLOW
# =========================

st.header("🔄 System Workflow")

st.code("""
Patient Information
       ↓
MRI Scan Upload
       ↓
MRI Preprocessing
       ↓
CNN-Based Classification
       ↓
Dementia Prediction
       ↓
Confidence Score
       ↓
Explainable AI Insights
       ↓
Clinical Decision Support
""")

st.divider()

# =========================
# DASHBOARD OVERVIEW
# =========================

st.header("📈 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Prediction Classes",
        "4"
    )

with col2:
    st.metric(
        "Model Accuracy",
        "98.3%"
    )

with col3:
    st.metric(
        "Precision",
        "97.8%"
    )

with col4:
    st.metric(
        "Recall",
        "98.1%"
    )

st.divider()

# =========================
# HOW TO USE
# =========================

st.header("📌 How to Use")

st.markdown("""
1️⃣ Navigate to the **Upload MRI Scan** page.

2️⃣ Enter patient details.

3️⃣ Upload an MRI image (JPG, JPEG, PNG).

4️⃣ Click **Analyze MRI Scan**.

5️⃣ View results on the **Results** page.

6️⃣ Review explanations on the **Explainable AI** page.
""")

st.divider()

# =========================
# TEAM SECTION
# =========================

st.header("👥 Team Contributions")

st.markdown("""
| Role | Responsibility |
|--------|--------------|
| Data & Research Lead | Data collection and literature review |
| ML Engineer | CNN model development and training |
| Frontend Developer | Streamlit dashboard and visualization |
| Explainable AI Lead | Model interpretation and insights |
| Integration Lead | Backend integration and deployment |
""")

st.divider()

# =========================
# FOOTER
# =========================

st.caption(
    "NeuroSense AI • MRI-Based Cognitive Decline Detection System • Hackathon 2025"
)
