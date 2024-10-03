"""This file is to generate a Pylint badge"""
import os
import re

# Path to the Pylint report file
pylint_report_file = os.path.abspath('../post_traces/pylint_results.txt')

# Read the Pylint report file
with open(pylint_report_file, 'r', encoding='utf-8') as file:
    pylint_output = file.read()

# Extract the Pylint score using regex
match = re.search(r'rated at (\d+\.\d+)/10', pylint_output)
if match:
    pylint_score = round(float(match.group(1)))  # Round the score to the nearest integer
else:
    pylint_score = 0  # Default score if not found

print(f"Pylint Score: {pylint_score}/10")

def generate_badge(score, badge_path="pylint-badge.svg"):
    """Generate an SVG badge indicating the Pylint score.

    Args:
        score (int): The Pylint score.
        badge_path (str): The path where the badge will be saved.
    """
    # Determine the badge color based on Pylint score
    if score >= 9:
        color = "#4c1"  # Green
    elif score >= 8:
        color = "#FFFF00"  # Yellow
    elif score >= 5:
        color = "#FFA500"  # Orange
    else:
        color = "#FF0000"  # Red

    # SVG content for the badge
    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
    <linearGradient id="a" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <rect rx="3" width="100" height="20" fill="#555"/>
    <rect rx="3" x="45" width="55" height="20" fill="#4c1"/> 
    <path fill="{color}" d="M45 0h5v20h-5z"/> 
    <rect rx="3" width="100" height="20" fill="url(#a)"/>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
        <text x="23" y="15" fill="#010101" fill-opacity="0">Pylint</text>
        <text x="23" y="14">Pylint</text>
        <text x="77" y="15" fill="#010101" fill-opacity="0">{score}/10</text>
        <text x="77" y="14">{score}/10</text>
    </g>
</svg>
"""

    # Write the SVG content to a file
    print(f"Writing SVG to {badge_path} with Pylint score {score}/10")
    with open(badge_path, "w", encoding='utf-8') as badge_file:
        badge_file.write(svg)

# Path where the badge will be saved
badge_file_path = os.path.abspath("pylint-badge.svg")

# Generate the badge
generate_badge(pylint_score, badge_file_path)
