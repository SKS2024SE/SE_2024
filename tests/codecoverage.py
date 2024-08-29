import json

# Path to your JSON file
file_path = '/workspaces/SE_2024/coverage.json'

# Open and load the JSON data
with open(file_path, 'r') as file:
    coverage_data = json.load(file)

# Extract the total coverage percentage from the 'totals' section
total_coverage = coverage_data.get('totals', {}).get('percent_covered', 0)

print(f"Total Coverage: {total_coverage}%")

def generate_badge(coverage, output_path="coverage-badge.svg"):
    # Determine the badge color based on coverage percentage
    if coverage >= 90:
        color = "#4c1"
    elif coverage >= 75:
        color = "#FFFF00"
    elif coverage >= 50:
        color = "#FFA500"
    else:
        color = "#FF0000"

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
        <text x="23" y="15" fill="#010101" fill-opacity="0">coverage</text>
        <text x="23" y="14">Cov</text>
        <text x="77" y="15" fill="#010101" fill-opacity="0">{coverage}%</text>
        <text x="77" y="14">{coverage}%</text>
    </g>
</svg>
"""

    # Write the SVG content to a file
    with open(output_path, "w") as f:
        f.write(svg)

# Generate the badge
generate_badge(total_coverage)

