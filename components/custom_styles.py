import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Move sidebar down by 200px */
        section[data-testid="stSidebar"] {
            margin-top: -200px;
        }
        
        /* Adjust main content area to align with moved sidebar */
        .main .block-container {
            padding-top: 2rem;
            margin-top: -200px;
        }
        
        /* Ensure proper spacing for sidebar content */
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            padding-top: 0rem;
        }
        
        /* Additional styling for clean layout */
        .stApp {
            margin-top: 0;
        }
        </style>
    """, unsafe_allow_html=True)