import streamlit as st
from datetime import datetime

def create_alert(message, alert_type="info", icon="info-circle"):
    """Create a styled alert message"""
    colors = {
        "info": "#0dcaf0",
        "success": "#198754",
        "warning": "#ffc107",
        "danger": "#dc3545"
    }
    
    st.markdown(f"""
        <div style="
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: {colors[alert_type]}15;
            border-left: 4px solid {colors[alert_type]};
            margin-bottom: 1rem;
        ">
            <i class="fas fa-{icon}"></i> {message}
        </div>
    """, unsafe_allow_html=True)

def notification_system():
    """Initialize and manage notifications"""
    if 'notifications' not in st.session_state:
        st.session_state.notifications = []
    
    def add_notification(message, level="info"):
        st.session_state.notifications.append({
            "message": message,
            "level": level,
            "timestamp": datetime.now()
        })
    
    return add_notification 