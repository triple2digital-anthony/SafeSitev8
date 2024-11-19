import streamlit as st
from components.navigation import create_modern_navigation
from pages import dashboard, threat_analysis, behavioral_patterns, video_upload, settings

def main():
    selected = create_modern_navigation()
    
    if selected == "Dashboard":
        dashboard.show_dashboard()
    elif selected == "Threat Analysis":
        threat_analysis.show_threat_analysis()
    elif selected == "Behavioral Patterns":
        behavioral_patterns.show_behavioral_patterns()
    elif selected == "Video Upload":
        video_upload.show_video_upload()
    elif selected == "Settings":
        settings.show_settings()

if __name__ == "__main__":
    main()
