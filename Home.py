import streamlit as st
from pages.dashboard import show_dashboard
from pages.threat_analysis import show_threat_analysis
from pages.behavioral_patterns import show_behavioral_patterns
from pages.settings import show_settings
from pages.video_upload import show_video_upload

# Configure the page
st.set_page_config(
    page_title="Safe Site Security Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the sidebar
st.markdown("""
    <style>
    .sidebar-nav {
        padding: 10px;
    }
    .nav-link {
        display: flex;
        align-items: center;
        padding: 10px;
        text-decoration: none;
        color: #262730;
        margin-bottom: 5px;
        border-radius: 5px;
    }
    .nav-link:hover {
        background-color: #f0f2f6;
    }
    .nav-link.active {
        background-color: #0068c9;
        color: white;
    }
    .nav-icon {
        margin-right: 10px;
        width: 24px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("Safe Site")
    
    # Dictionary of pages with their icons and functions
    pages = {
        "Dashboard": ("📊", show_dashboard),
        "Threat Analysis": ("⚠️", show_threat_analysis),
        "Video Upload": ("📹", show_video_upload),
        "Behavioral Patterns": ("📈", show_behavioral_patterns),
        "Settings": ("⚙️", show_settings)
    }
    
    # Create navigation menu
    selected_page = st.sidebar.radio(
        "",
        list(pages.keys()),
        format_func=lambda x: f"{pages[x][0]} {x}"
    )
    
    # Display selected page
    pages[selected_page][1]()
    
    # Add any additional sidebar widgets below navigation
    with st.sidebar:
        st.markdown("---")
        st.markdown("### System Status")
        st.success("All Systems Operational")
        
        # Add any other sidebar widgets you had before
        st.markdown("### Quick Stats")
        st.metric("Active Cameras", "12")
        st.metric("Alert Level", "Low")

if __name__ == "__main__":
    main() 