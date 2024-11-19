#!/bin/bash

# Enable error reporting and debugging
set -e
set -x

# Define the project root directory
PROJECT_ROOT="/Users/anthonydiprizio/Downloads/SafeSitev8"

echo "Creating Safe Site project structure at: $PROJECT_ROOT"

# Create main project directories
mkdir -p "$PROJECT_ROOT"/{.streamlit,pages,components,utils,assets/{videos,images,styles},cache,models}

# Create Python package files
touch "$PROJECT_ROOT"/__init__.py
touch "$PROJECT_ROOT"/components/__init__.py
touch "$PROJECT_ROOT"/utils/__init__.py

# Create Streamlit config
cat > "$PROJECT_ROOT"/.streamlit/config.toml << 'EOL'
[server]
port = 8501
headless = true
maxUploadSize = 500
enableXsrfProtection = true
enableCORS = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
EOL

# Create requirements.txt
cat > "$PROJECT_ROOT"/requirements.txt << 'EOL'
streamlit==1.28.0
pandas==2.0.0
plotly==5.18.0
opencv-python==4.10.0.84
scikit-learn==1.3.0
streamlit-extras==0.3.0
streamlit-option-menu==0.3.2
numpy==1.24.0
Pillow==10.0.0
torch==1.12.0
torchvision==0.13.0
matplotlib==3.5.0

# Create main application file
cat > "$PROJECT_ROOT"/app.py << 'EOL'
import streamlit as st
from components.navigation import create_navigation
from components.custom_styles import apply_custom_styles

st.set_page_config(
    page_title="Safe Site",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    apply_custom_styles()
    selected_page = create_navigation()
    
if __name__ == "__main__":
    main()
EOL

echo "Project setup completed successfully!" 