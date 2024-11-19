import streamlit as st
from streamlit_option_menu import option_menu

def create_navigation():
    with st.sidebar:
        selected = option_menu(
            "Safe Site",
            ["Dashboard", "Threat Analysis", "Behavioral Patterns", "Settings"],
            icons=['speedometer', 'exclamation-triangle', 'activity', 'gear'],
            menu_icon="shield-lock",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#f0f2f6"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
                "nav-link-selected": {"background-color": "#1f77b4"},
            }
        )
    return selected 