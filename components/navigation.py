import streamlit as st
from streamlit_option_menu import option_menu

def create_modern_navigation():
    # Custom CSS for modern styling
    st.markdown("""
        <style>
        .nav-link {
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            margin: 0.2rem 0;
            transition: all 0.3s ease;
        }
        .nav-link:hover {
            background-color: rgba(255, 255, 255, 0.1);
            transform: translateX(5px);
        }
        .nav-link-selected {
            border-left: 4px solid #1f77b4;
            font-weight: 600;
            background-color: rgba(31, 119, 180, 0.1) !important;
        }
        .company-logo {
            text-align: center;
            padding: 1.5rem 0;
        }
        .status-indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        .status-active {
            background-color: #28a745;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # Company Logo/Name Section
        st.markdown("""
            <div class="company-logo">
                <h2>🛡️ Safe Site</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Modern Navigation Menu
        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard", 
                "Threat Analysis",
                "Behavioral Patterns",
                "Video Upload",
                "Settings"
            ],
            icons=[
                'speedometer2',
                'shield-exclamation',
                'people-fill',
                'camera-video-fill',
                'gear-fill'
            ],
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "transparent"
                },
                "icon": {
                    "font-size": "1rem",
                    "margin-right": "0.5rem"
                },
                "nav-link": {
                    "font-size": "0.9rem",
                    "text-align": "left",
                    "padding": "0.75rem",
                    "margin": "0.2rem 0",
                    "border-radius": "0.5rem"
                },
                "nav-link-selected": {
                    "background-color": "rgba(31, 119, 180, 0.1)",
                    "font-weight": "600"
                }
            }
        )
        
        # System Status Section
        st.markdown("### System Status")
        
        # Status indicators
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div>
                    <span class="status-indicator status-active"></span>
                    AI Engine
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div>
                    <span class="status-indicator status-active"></span>
                    Analytics
                </div>
            """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
            <div style='position: fixed; bottom: 0; padding: 1rem; font-size: 0.8rem; opacity: 0.7;'>
                Safe Site v1.0.0
            </div>
        """, unsafe_allow_html=True)

    return selected