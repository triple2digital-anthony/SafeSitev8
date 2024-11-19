import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Simulated data for each video
VIDEO_DATA = {
    'video_1.mp4': {
        'title': 'Weapon Detection - Main Entrance',
        'threat_level': 4.8,
        'confidence': 0.92,
        'objects_detected': ['Handgun', 'Backpack', 'Person'],
        'timestamp': '2024-03-19 14:23:01',
        'location': 'Main Entrance',
        'motion_intensity': 0.75,
        'crowd_density': 0.45,
        'behavioral_markers': ['Rapid Movement', 'Concealment Attempt']
    },
    'video_2.mp4': {
        'title': 'Fight Detection - Hallway B',
        'threat_level': 3.6,
        'confidence': 0.87,
        'objects_detected': ['Multiple Persons', 'Phone', 'Backpack'],
        'timestamp': '2024-03-19 14:25:15',
        'location': 'Hallway B',
        'motion_intensity': 0.89,
        'crowd_density': 0.65,
        'behavioral_markers': ['Aggressive Posture', 'Group Formation']
    },
    'video_3.mp4': {
        'title': 'Vandalism Detection - Cafeteria',
        'threat_level': 2.9,
        'confidence': 0.78,
        'objects_detected': ['Person', 'Spray Can', 'Bag'],
        'timestamp': '2024-03-19 14:30:00',
        'location': 'Cafeteria',
        'motion_intensity': 0.45,
        'crowd_density': 0.15,
        'behavioral_markers': ['Suspicious Loitering', 'Concealed Activity']
    }
}

def create_confidence_gauge(confidence):
    """Create a confidence score gauge"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Detection Confidence", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 60], 'color': "lightgray"},
                {'range': [60, 80], 'color': "gray"},
                {'range': [80, 100], 'color': "darkblue"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(height=200, margin=dict(l=10, r=10, t=30, b=10))
    return fig

def create_motion_analysis(motion_data):
    """Create motion analysis line chart"""
    fig = go.Figure()
    
    # Simulate motion data points
    x = list(range(30))
    y = [motion_data * np.random.uniform(0.8, 1.2) for _ in range(30)]
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines+markers',
        name='Motion Intensity',
        line=dict(color='#1f77b4', width=2),
        fill='tozeroy'
    ))
    
    fig.update_layout(
        title="Motion Analysis",
        height=200,
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis_title="Time (s)",
        yaxis_title="Intensity"
    )
    return fig

def create_crowd_density_map():
    """Create crowd density heatmap"""
    x = np.linspace(-1, 1, 20)
    y = np.linspace(-1, 1, 20)
    X, Y = np.meshgrid(x, y)
    Z = np.random.rand(20, 20)
    
    fig = go.Figure(data=go.Heatmap(
        z=Z,
        colorscale='Viridis',
        showscale=True
    ))
    
    fig.update_layout(
        title="Crowd Density Map",
        height=250,
        margin=dict(l=10, r=10, t=30, b=10)
    )
    return fig

def show_threat_analysis():
    st.title("Threat Analysis")
    
    # Video selector
    video_files = list(VIDEO_DATA.keys())
    selected_video = st.selectbox("Select Video Feed", video_files)
    video_data = VIDEO_DATA[selected_video]
    
    # Main content columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Video player
        st.subheader(video_data['title'])
        st.video(f"assets/videos/{selected_video}")
        
        # Detection details
        st.markdown(f"""
        **Location:** {video_data['location']}  
        **Timestamp:** {video_data['timestamp']}  
        **Objects Detected:** {', '.join(video_data['objects_detected'])}
        """)
        
        # Behavioral markers
        st.markdown("### Behavioral Markers")
        for marker in video_data['behavioral_markers']:
            st.markdown(f"- {marker}")
        
        # Motion analysis
        motion_fig = create_motion_analysis(video_data['motion_intensity'])
        st.plotly_chart(motion_fig, use_container_width=True)
    
    with col2:
        # Confidence score
        confidence_gauge = create_confidence_gauge(video_data['confidence'])
        st.plotly_chart(confidence_gauge, use_container_width=True)
        
        # Threat metrics
        st.metric(
            label="Threat Level",
            value=f"{video_data['threat_level']:.1f}/5.0",
            delta=f"{video_data['threat_level'] - 2.5:.1f} from baseline"
        )
        
        st.metric(
            label="Crowd Density",
            value=f"{video_data['crowd_density']*100:.0f}%",
            delta=f"{(video_data['crowd_density']-0.5)*100:.0f}% from average"
        )
        
        # Alert status
        alert_status = "🚨 HIGH ALERT" if video_data['threat_level'] > 4 else "⚠️ MONITORING"
        st.markdown(f"""
        <div style='padding: 1rem; background-color: {'#ff4b4b' if video_data['threat_level'] > 4 else '#ffa600'}; 
                    border-radius: 10px; text-align: center; color: white; font-weight: bold;'>
            {alert_status}
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom section
    st.markdown("---")
    
    # Crowd density map
    st.subheader("Spatial Analysis")
    density_map = create_crowd_density_map()
    st.plotly_chart(density_map, use_container_width=True)
    
    # Action buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("🚨 Trigger Alert")
    with col2:
        st.button("👮 Notify Security")
    with col3:
        st.button("📱 Send SMS")
    with col4:
        st.button("📝 Generate Report")
    
    # Historical data
    st.markdown("### Historical Analysis")
    historical_data = pd.DataFrame({
        'Time': pd.date_range(start='2024-03-19', periods=24, freq='H'),
        'Threat Level': np.random.uniform(1, 5, 24),
        'Incidents': np.random.randint(0, 5, 24)
    })
    
    fig = px.line(historical_data, x='Time', y=['Threat Level', 'Incidents'],
                  title='24-Hour Threat History')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    show_threat_analysis()