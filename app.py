import streamlit as st


st.set_page_config(
    page_title="NeuroSense AI",
    page_icon="🧠",
    layout="wide"
)


# Title
st.title("🧠 NeuroSense AI")

st.subheader(
    "Brain-Inspired Cognitive Decline Detection System"
)


st.markdown(
"""
### About the Project

NeuroSense AI is an intelligent healthcare support system
that uses **Spiking Neural Networks (SNN)** to analyze
cognitive patterns and identify early signs of cognitive decline.

The system combines:
- 🧠 Neuromorphic Computing
- 🤖 Artificial Intelligence
- 📊 Data Analysis
- 🔍 Explainable AI
"""
)


st.divider()


col1, col2, col3 = st.columns(3)


with col1:
    st.info(
        """
        ### 🧠 SNN Model
        
        Brain-inspired neural
        processing using spikes.
        """
    )


with col2:
    st.success(
        """
        ### 📊 Data Analysis
        
        Analyze cognitive
        patterns and features.
        """
    )


with col3:
    st.warning(
        """
        ### 🔍 Explainability
        
        Understand why AI
        gives predictions.
        """
    )


st.divider()


st.write(
"Use the navigation menu on the left to start analysis."
)