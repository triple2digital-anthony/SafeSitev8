import streamlit as st
from pages.dashboard import show_dashboard
from pages.threat_analysis import show_threat_analysis
from pages.behavioral_patterns import show_behavioral_patterns
from pages.settings import show_settings
from pages.video_upload import show_video_upload

def main():
    # Add custom CSS for modern styling
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .sidebar .sidebar-content h2 {
            color: #333;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .sidebar .sidebar-content .stRadio > div {
            display: flex;
            flex-direction: column;
        }
        .sidebar .sidebar-content .stRadio > div > label {
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: background-color 0.3s, box-shadow 0.3s;
            font-weight: 500;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .sidebar .sidebar-content .stRadio > div > label:hover {
            background-color: #e0e0e0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .sidebar .sidebar-content .stRadio > div > label[data-selected="true"] {
            background-color: #007bff;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        .sidebar .sidebar-content .stRadio > div > label > span {
            margin-right: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Safe Site")
    
    st.sidebar.markdown("# Navigation")
    page = st.sidebar.radio(
        "",
        [
            "📊 Dashboard",
            "⚠️ Threat Analysis", 
            "📹 Video Upload",
            "📈 Behavioral Patterns",
            "⚙️ Settings"
        ],
        label_visibility="collapsed"
    )
    
    # Display the selected page
    if page == "📊 Dashboard":
        show_dashboard()
    elif page == "⚠️ Threat Analysis":
        show_threat_analysis()
    elif page == "📹 Video Upload":
        show_video_upload()
    elif page == "📈 Behavioral Patterns":
        show_behavioral_patterns()
    elif page == "⚙️ Settings":
        show_settings()

if __name__ == "__main__":
    main()
