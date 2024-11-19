import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_threat_gauge(threat_level):
    """Create an animated threat level gauge"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=threat_level,
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 3, 'increasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 5], 'tickwidth': 1},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 1], 'color': 'lightgreen'},
                {'range': [1, 2], 'color': 'yellow'},
                {'range': [2, 3], 'color': 'orange'},
                {'range': [3, 4], 'color': 'red'},
                {'range': [4, 5], 'color': 'darkred'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': threat_level
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#ffffff", 'family': "Arial"}
    )
    return fig

def create_activity_heatmap(data):
    """Create activity heatmap by hour and day"""
    fig = px.imshow(
        data,
        labels=dict(x="Hour of Day", y="Day of Week", color="Activity Level"),
        x=[f"{i:02d}:00" for i in range(24)],
        y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        color_continuous_scale="Viridis"
    )
    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def show_dashboard():
    st.title("Safe Site Operations Dashboard")
    
    # Create three columns for top metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Active Alerts",
            value=12,
            delta="3 ↑",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label="Response Time",
            value="1.2s",
            delta="-0.3s",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="System Health",
            value="98%",
            delta="2% ↑",
            delta_color="normal"
        )

    # Create two columns for main content
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.subheader("Threat Level Monitor")
        threat_gauge = create_threat_gauge(3.8)
        st.plotly_chart(threat_gauge, use_container_width=True)
        
        # Activity heatmap
        st.subheader("Activity Patterns")
        # Simulate activity data
        activity_data = np.random.rand(7, 24)
        heatmap = create_activity_heatmap(activity_data)
        st.plotly_chart(heatmap, use_container_width=True)

    with right_col:
        st.subheader("Recent Alerts")
        with st.container():
            # Custom CSS for alerts
            st.markdown("""
                <style>
                .alert-card {
                    padding: 1rem;
                    border-radius: 10px;
                    margin-bottom: 1rem;
                    background-color: rgba(255, 255, 255, 0.1);
                    border-left: 4px solid;
                }
                .alert-high { border-left-color: #ff4b4b; }
                .alert-medium { border-left-color: #ffa600; }
                .alert-low { border-left-color: #00cc44; }
                </style>
            """, unsafe_allow_html=True)
            
            # Sample alerts
            alerts = [
                {"level": "high", "message": "Unauthorized access detected", "time": "2 mins ago"},
                {"level": "medium", "message": "Unusual activity in Sector B", "time": "15 mins ago"},
                {"level": "low", "message": "System update required", "time": "1 hour ago"},
            ]
            
            for alert in alerts:
                st.markdown(f"""
                    <div class="alert-card alert-{alert['level']}">
                        <small>{alert['time']}</small>
                        <h4 style="margin: 0">{alert['message']}</h4>
                    </div>
                """, unsafe_allow_html=True)
        
        # Quick Actions
        st.subheader("Quick Actions")
        col1, col2 = st.columns(2)
        with col1:
            st.button("🚨 Trigger Alarm")
            st.button("🔒 Lockdown")
        with col2:
            st.button("📱 Send Alert")
            st.button("📸 View Cameras")
            
        # System Status
        st.subheader("System Status")
        status_data = {
            "Camera Network": 98,
            "Motion Sensors": 100,
            "Access Control": 95,
            "Alert System": 100
        }
        
        for system, status in status_data.items():
            st.progress(status/100, text=f"{system}: {status}%")

if __name__ == "__main__":
    show_dashboard()