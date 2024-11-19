import streamlit as st
from components.navigation import create_navigation
from utils.cache_manager import initialize_cache
from components.custom_styles import apply_custom_styles

st.set_page_config(
    page_title="Safe Site",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS styles
apply_custom_styles()

# Initialize cache and session state
initialize_cache()

def main():
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Dashboard"
    
    selected_page = create_navigation()
    
    if selected_page == "Dashboard":
        from pages.dashboard import main as show_dashboard
        show_dashboard()
    elif selected_page == "Threat Analysis":
        from pages.threat_analysis import main as show_threat_analysis
        show_threat_analysis()
    elif selected_page == "Behavioral Patterns":
        from pages.behavioral_patterns import main as show_behavioral_patterns
        show_behavioral_patterns()
    elif selected_page == "Settings":
        from pages.settings import main as show_settings
        show_settings()
    else:
        st.error("Page not found.")

if __name__ == "__main__":
    main()
