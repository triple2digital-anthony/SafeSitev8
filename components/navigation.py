import streamlit as st
from streamlit_option_menu import option_menu

def create_navigation():
    with st.sidebar:
        # Logo/branding section
        st.image("assets/images/logo.png", width=200)
        
        selected = option_menu(
            menu_title="Safe Site",
            options=[
                "Dashboard", 
                "Threat Analysis",
                "Behavioral Patterns",
                "Settings"
            ],
            icons=[
                'speedometer2',
                'shield-exclamation',
                'graph-up',
                'gear'
            ],
            menu_icon="shield-lock",
            default_index=0,
            styles={
                "container": {
                    "padding": "1rem",
                    "background-color": "#f8f9fa",
                    "border-radius": "0.5rem",
                },
                "icon": {
                    "color": "#1f77b4", 
                    "font-size": "1rem"
                },
                "nav-link": {
                    "font-size": "0.9rem",
                    "text-align": "left",
                    "margin": "0.2rem",
                    "padding": "0.8rem",
                    "--hover-color": "#eee",
                    "border-radius": "0.3rem",
                },
                "nav-link-selected": {
                    "background-color": "#1f77b4",
                    "color": "white",
                },
            }
        )
        
        # System status section
        st.sidebar.markdown("---")
        with st.sidebar.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown('<span class="status-indicator status-active"></span>', unsafe_allow_html=True)
            with col2:
                st.markdown("**System Status:** Online")
        
        # Quick stats
        st.sidebar.markdown("### Quick Stats")
        st.sidebar.metric("Active Alerts", "5", "+2")
        st.sidebar.metric("Response Time", "1.2s", "-0.3s")
        
        return selected 