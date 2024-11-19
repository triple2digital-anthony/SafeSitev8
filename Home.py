import streamlit as st
from pages.dashboard import show_dashboard
from pages.threat_analysis import show_threat_analysis
from pages.video_upload import show_video_upload

# Configure the page
st.set_page_config(
    page_title="Safe Site Security Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match the screenshot exactly
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    
    /* Navigation item styling to match screenshot */
    div[data-testid="stRadio"] > div {
        padding: 0;
    }
    
    div[data-testid="stRadio"] label {
        display: flex;
        align-items: center;
        padding: 0.5rem 1rem;
        cursor: pointer;
        border-radius: 0.5rem;
        margin: 0.2rem 0;
    }
    
    div[data-testid="stRadio"] label:hover {
        background-color: #f0f2f6;
    }
    
    div[data-testid="stRadio"] label[data-checked="true"] {
        background-color: #0068c9;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    
    pages = {
        "Live Dashboard": show_dashboard,
        "Threat Analysis": show_threat_analysis,
        "Video Upload": show_video_upload
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main() 