import streamlit as st
import cv2
import tempfile
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def show_video_upload():
    st.title("Video Upload & Analysis")
    
    # Create two columns for upload and status
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Upload video for security analysis", 
            type=['mp4', 'avi', 'mov']
        )
        
        if uploaded_file:
            # Save uploaded file
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            
            # Video preview
            st.video(tfile.name)
            
            # Process video with progress tracking
            with st.spinner("Analyzing video for security threats..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Process the video
                results = process_video(tfile.name, progress_bar, status_text)
                
                # Display results
                display_analysis_results(results)
    
    with col2:
        st.info("Upload a video to analyze for:")
        st.markdown("""
        - 🎯 Threat Detection
        - 👥 Person Tracking
        - ⚠️ Suspicious Activity
        - 🔍 Object Detection
        - 📊 Motion Analysis
        """)

def process_video(video_path, progress_bar, status_text):
    """Process video and return analysis results"""
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    results = {
        'threat_levels': [],
        'motion_scores': [],
        'object_counts': [],
        'timestamps': [],
        'detected_objects': []
    }
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Update progress
        progress = int((frame_count / total_frames) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Processing frame {frame_count}/{total_frames}")
        
        # Simulate analysis (replace with actual analysis)
        results['threat_levels'].append(np.random.uniform(1, 5))
        results['motion_scores'].append(np.random.uniform(0, 1))
        results['object_counts'].append(np.random.randint(0, 10))
        results['timestamps'].append(frame_count/fps)
        
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
        st.metric("Average Threat Level", 
                 f"{np.mean(results['threat_levels']):.2f}")
    with col2:
        st.metric("Peak Motion Score", 
                 f"{max(results['motion_scores']):.2f}")
    with col3:
        st.metric("Total Objects", 
                 sum(results['object_counts']))

    # Threat level gauge
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=np.mean(results['threat_levels']),
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
    
    # Time series analysis
    col1, col2 = st.columns(2)
    
    with col1:
        fig_threat = px.line(
            x=results['timestamps'],
            y=results['threat_levels'],
            title="Threat Level Timeline",
            labels={"x": "Time (s)", "y": "Threat Level"}
        )
        st.plotly_chart(fig_threat)
    
    with col2:
        fig_motion = px.line(
            x=results['timestamps'],
            y=results['motion_scores'],
            title="Motion Analysis",
            labels={"x": "Time (s)", "y": "Motion Score"}
        )
        st.plotly_chart(fig_motion)
    
    # Export options
    st.download_button(
        "Download Analysis Report",
        data=generate_report(results),
        file_name=f"security_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

def generate_report(results):
    """Generate a text report of the analysis"""
    report = f"""Security Analysis Report
Generated: {datetime.now()}
    
Summary:
- Average Threat Level: {np.mean(results['threat_levels']):.2f}
- Peak Motion Score: {max(results['motion_scores']):.2f}
- Total Objects Detected: {sum(results['object_counts'])}
"""
    return report

if __name__ == "__main__":
    show_video_upload() 