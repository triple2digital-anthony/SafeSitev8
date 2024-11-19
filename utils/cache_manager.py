import streamlit as st
import os
import json

@st.cache_resource
def initialize_cache():
    """Initialize cache for storing processed data"""
    if 'cache' not in st.session_state:
        st.session_state.cache = {
            'processed_videos': {},
            'alerts': [],
            'metrics': {
                'threat_level': 'Low',
                'active_alerts': 0,
                'response_time': '00:00',
            }
        }
    return st.session_state.cache

def save_to_cache(key, data):
    """Save data to cache file"""
    cache_dir = 'cache'
    os.makedirs(cache_dir, exist_ok=True)
    cache_file = os.path.join(cache_dir, f'{key}.json')
    with open(cache_file, 'w') as f:
        json.dump(data, f)

def load_from_cache(key):
    """Load data from cache file"""
    cache_dir = 'cache'
    cache_file = os.path.join(cache_dir, f'{key}.json')
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    return None