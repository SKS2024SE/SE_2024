import os
import re

def extract_pylint_score_from_file(file_path):
    """Extract the Pylint score from a given file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    match = re.search(r'rated at (\d+\.\d+)/10', content)
    if match:
        return round(float(match.group(1)))
    return 0

def generate_pylint_badge(score, badge_path="pylint-badge.svg"):
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
        <text x="77" y="15" fill="#010101" fill-opacity="0">{score}</text>
        <text x="77" y="14">{score}</text>
    </g>
</svg>
"""

    # Write the SVG content to a file
    print(f"Writing SVG to {badge_path} with Pylint score {score}/10")
    with open(badge_path, "w", encoding='utf-8') as badge_file:
        badge_file.write(svg)

def main(pylint_report_file):
    """Main function to extract score from file and generate the badge."""
    score = extract_pylint_score_from_file(pylint_report_file)
    print(f"Extracted Pylint Score: {score}")
    
    badge_file_path = os.path.abspath("pylint-badge.svg")
    generate_pylint_badge(score, badge_file_path)

if __name__ == "__main__":
    # Specify the path to your Pylint report file
    pylint_report_file = os.path.abspath('/workspaces/SE_2024/post_traces/pylint_results.txt')
 # Update this path
    main(pylint_report_file)
