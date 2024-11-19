import streamlit as st
import cv2
import tempfile
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def show_video_upload():
    st.title("Video Upload & Analysis")
    
    # Create two columns for upload and preview
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # File uploader
        uploaded_file = st.file_uploader(
            "Upload video for security analysis", 
            type=['mp4', 'avi', 'mov'],
            help="Upload a video file to analyze for security threats"
        )
        
        if uploaded_file:
            # Save uploaded file temporarily
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            
            # Show video preview
            st.video(tfile.name)
            
            # Process video with progress bar
            with st.spinner("Analyzing video..."):
                progress_bar = st.progress(0)
                results = process_video(tfile.name, progress_bar)
                
            # Display results
            display_analysis_results(results)
    
    with col2:
        st.info("Upload a video to begin analysis. The system will scan for:")
        st.markdown("""
        - 🎯 Threat Detection
        - 👥 Person Tracking
        - ⚠️ Suspicious Activity
        - 🔍 Object Detection
        - 📊 Motion Analysis
        """)

def process_video(video_path, progress_bar):
    """Process video and return analysis results"""
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    results = {
        'threat_levels': [],
        'motion_scores': [],
        'detected_objects': [],
        'timestamps': [],
        'alerts': []
    }
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Update progress
        progress = int((frame_count / total_frames) * 100)
        progress_bar.progress(progress)
        
        # Simulate analysis (replace with actual analysis)
        results['threat_levels'].append(np.random.uniform(1, 5))
        results['motion_scores'].append(np.random.uniform(0, 1))
        results['detected_objects'].append(['Person', 'Bag'][np.random.randint(0, 2)])
        results['timestamps'].append(frame_count / 30)  # Assuming 30 fps
        
        if np.random.random() < 0.1:  # 10% chance of alert
            results['alerts'].append({
                'time': frame_count / 30,
                'type': 'Suspicious Activity',
                'confidence': np.random.uniform(0.7, 0.99)
            })
        
        frame_count += 1
        time.sleep(0.01)  # Simulate processing time
        
    cap.release()
    return results

def display_analysis_results(results):
    """Display analysis results in an organized dashboard"""
    st.subheader("Analysis Results")
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        avg_threat = np.mean(results['threat_levels'])
        st.metric("Average Threat Level", f"{avg_threat:.2f}")
    with col2:
        max_motion = max(results['motion_scores'])
        st.metric("Peak Motion Score", f"{max_motion:.2f}")
    with col3:
        alert_count = len(results['alerts'])
        st.metric("Total Alerts", alert_count)
    
    # Threat level gauge
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_threat,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 5]},
            'steps': [
                {'range': [0, 2], 'color': "lightgreen"},
                {'range': [2, 3.5], 'color': "yellow"},
                {'range': [3.5, 5], 'color': "red"}
            ]
        }
    ))
    st.plotly_chart(fig_gauge)
    
    # Time series plots
    fig_time = px.line(
        x=results['timestamps'],
        y=results['threat_levels'],
        title="Threat Level Over Time",
        labels={"x": "Time (s)", "y": "Threat Level"}
    )
    st.plotly_chart(fig_time)
    
    # Alerts table
    if results['alerts']:
        st.subheader("Security Alerts")
        alert_data = pd.DataFrame(results['alerts'])
        st.dataframe(alert_data)

if __name__ == "__main__":
    show_video_upload()