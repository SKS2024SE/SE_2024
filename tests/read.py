import json


with open("coverage.json", "r") as f:
    coverage_data = json.load(f)


total_coverage = coverage_data['totals']['percent_covered']

print(f"Total Coverage: {total_coverage}%")

