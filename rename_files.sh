#!/bin/bash

cd pages

# Remove all unnecessary files
rm -f 1_Plotting_Demo.py 2_Mapping_Demo.py 3_DataFrame_Demo.py
rm -f about.py dashboard.py home.py settings.py threat_analysis.py

# Ensure we only have our four main pages with correct names
files=(
    "1_dashboard.py"
    "2_threat_analysis.py"
    "3_behavioral_patterns.py"
    "4_settings.py"
)

# Check and keep only the files we need
for file in *; do
    if [[ ! " ${files[@]} " =~ " ${file} " ]]; then
        rm -f "$file"
    fi
done

echo "Cleaned up pages directory!"