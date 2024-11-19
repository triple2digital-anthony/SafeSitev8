import streamlit as st
from components.navigation import create_navigation
from components.custom_styles import apply_custom_styles
from utils.cache_manager import initialize_cache

# Page configuration
st.set_page_config(
    page_title="Safe Site",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state if not already done
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.current_page = "Dashboard"
    st.session_state.alert_count = 0
    st.session_state.threat_level = "Low"

def main():
    # Apply custom styling
    apply_custom_styles()
    
    # Initialize cache
    cache = initialize_cache()
    
    # Create navigation and get selected page
    selected_page = create_navigation()
    
    # Update session state
    st.session_state.current_page = selected_page
    
    # Route to appropriate page
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
