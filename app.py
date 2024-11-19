import streamlit as st
from components.navigation import create_navigation

def main():
    selected_page = create_navigation()
    
    if selected_page == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()
    elif selected_page == "Threat Analysis":
        from pages.threat_analysis import show_threat_analysis
        show_threat_analysis()
    elif selected_page == "Behavioral Patterns":
        from pages.behavioral_patterns import show_behavioral_patterns
        show_behavioral_patterns()
    elif selected_page == "Settings":
        from pages.settings import show_settings
        show_settings()

if __name__ == "__main__":
    main()
