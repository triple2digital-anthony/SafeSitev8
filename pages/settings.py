import streamlit as st

def show_settings():
    st.title("Settings")
    
    # Add settings components
    st.subheader("System Configuration")
    
    # Example settings
    st.slider("Detection Sensitivity", 0.0, 1.0, 0.7)
    st.checkbox("Enable Notifications")
    st.selectbox("Video Quality", ["Low", "Medium", "High"])

if __name__ == "__main__":
    show_settings() 