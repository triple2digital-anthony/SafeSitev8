import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
            /* Custom CSS styles */
            .reportview-container .main .block-container{
                padding-top: 2rem;
            }
            .sidebar .sidebar-content {
                padding-top: 2rem;
            }
            .css-1d391kg p {
                font-size: 18px;
            }
            /* Add more styles as needed */
        </style>
    """, unsafe_allow_html=True)