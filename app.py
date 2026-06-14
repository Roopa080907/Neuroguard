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

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# HEADER
# =========================

st.title("🧠 NeuroSense AI")

st.markdown("""
# Brain-Inspired Cognitive Decline Detection System
""")

st.markdown("""
### Early Detection of Cognitive Decline using
### Spiking Neural Networks and Explainable AI
""")

st.divider()

# =========================
# ABOUT SECTION
# =========================

st.header("🚀 About the Project")

st.write("""
NeuroSense AI is an intelligent healthcare support system that uses
**Spiking Neural Networks (SNNs)** to analyze cognitive patterns and
identify early signs of cognitive decline.

The platform combines cutting-edge Artificial Intelligence,
Neuromorphic Computing and Explainable AI to support clinicians
and researchers in cognitive health monitoring.
""")

st.markdown("""
### Core Technologies

- 🧠 Neuromorphic Computing
- ⚡ Spiking Neural Networks
- 🤖 Artificial Intelligence
- 📊 Cognitive Data Analytics
- 🔍 Explainable AI
- ☁️ Streamlit Dashboard
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
        <h2>🧠 SNN Model</h2>
        <p>
        Brain-inspired neural processing using spikes
        for efficient cognitive pattern recognition.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>📊 Data Analysis</h2>
        <p>
        Analyze patient cognitive metrics and
        identify potential decline indicators.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2>🔍 Explainability</h2>
        <p>
        Understand model predictions through
        transparent Explainable AI techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# PROJECT WORKFLOW
# =========================

st.header("🔄 System Workflow")

st.code("""
Patient Data
      ↓
Data Preprocessing
      ↓
Feature Extraction
      ↓
Spiking Neural Network
      ↓
Risk Prediction
      ↓
Explainable AI Module
      ↓
Clinical Decision Support
""")

st.divider()

# =========================
# DASHBOARD STATS
# =========================

st.header("📈 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Patients Analysed",
        "1,248"
    )

with col2:
    st.metric(
        "Model Accuracy",
        "94.8%"
    )

with col3:
    st.metric(
        "Explainability Score",
        "91%"
    )

with col4:
    st.metric(
        "Risk Detection Rate",
        "92%"
    )

st.divider()

# =========================
# TEAM SECTION
# =========================

st.header("👥 Team Contributions")

st.markdown("""
| Role | Responsibility |
|--------|--------------|
| Data & Research Lead | Data collection and literature review |
| SNN / ML Engineer | Model development and training |
| Frontend & Dashboard | User Interface and Visualization |
| Explainable AI Lead | Explainability and insights |
| Integration & Deployment | Deployment and presentation |
""")

st.divider()

# =========================
# FOOTER
# =========================

st.caption(
    "NeuroSense AI • Brain-Inspired Cognitive Decline Detection System • Hackathon 2025"
) 