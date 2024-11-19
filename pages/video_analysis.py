import streamlit as st
import cv2
import tempfile
import time
from streamlit_webrtc import webrtc_streamer
import av
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

def process_uploaded_video():
    st.title("Video Upload & Analysis")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a video for analysis", type=['mp4', 'avi', 'mov'])
    
    if uploaded_file is not None:
        # Create a temporary file to store the video
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        
        # Video processing section
        st.subheader("Video Analysis")
        col1, col2 = st.columns([2,1])
        
        with col1:
            # Video player
            st.video(tfile.name)
            
        with col2:
            # Processing status
            with st.spinner("Analyzing video..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Get video properties
                cap = cv2.VideoCapture(tfile.name)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                duration = total_frames/fps
                
                # Initialize analysis metrics
                threat_levels = []
                motion_scores = []
                object_counts = []
                timestamps = []
                
                # Process each frame
                frame_count = 0
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                        
                    # Simulate analysis (replace with your actual analysis)
                    frame_count += 1
                    progress = int((frame_count/total_frames) * 100)
                    progress_bar.progress(progress)
                    status_text.text(f"Processing frame {frame_count}/{total_frames}")
                    
                    # Calculate metrics (replace with actual metrics)
                    threat_levels.append(np.random.uniform(1, 5))
                    motion_scores.append(np.random.uniform(0, 1))
                    object_counts.append(np.random.randint(0, 10))
                    timestamps.append(frame_count/fps)
                    
                    time.sleep(0.01)  # Simulate processing time
                
                cap.release()
                
        # Display analysis results
        st.subheader("Analysis Results")
        
        # Threat level gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=np.mean(threat_levels),
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
        col1, col2 = st.columns(2)
        
        with col1:
            # Motion analysis
            fig_motion = px.line(
                x=timestamps, 
                y=motion_scores,
                title="Motion Analysis",
                labels={"x": "Time (s)", "y": "Motion Score"}
            )
            st.plotly_chart(fig_motion)
            
        with col2:
            # Object detection counts
            fig_objects = px.line(
                x=timestamps, 
                y=object_counts,
                title="Objects Detected",
                labels={"x": "Time (s)", "y": "Count"}
            )
            st.plotly_chart(fig_objects)
        
        # Summary metrics
        st.subheader("Summary")
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        with metrics_col1:
            st.metric("Average Threat Level", f"{np.mean(threat_levels):.2f}")
        with metrics_col2:
            st.metric("Peak Motion Score", f"{max(motion_scores):.2f}")
        with metrics_col3:
            st.metric("Total Objects Detected", sum(object_counts))
            
        # Download analysis report
        st.download_button(
            "Download Analysis Report",
            data=f"Analysis Report\nDate: {datetime.now()}\n...",
            file_name="video_analysis_report.txt"
        )

if __name__ == "__main__":
    process_uploaded_video() 