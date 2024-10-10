#!/bin/bash

# Input file variable
input_file="titanic.csv"
output_file="filtered_passengers.txt"

# Extract passengers from 2nd class who embarked at Southampton
awk -F, 'NR > 1 && $3 == "2" && $13 == "S"' "$input_file" | \
sed -e 's/female/F/g' -e 's/male/M/g' | \
awk -F, '
BEGIN { total_age = 0; count = 0; }
{
    # Print the entire modified line
    print $0;

    if ($7 != "" && $7 ~ /^[0-9]+(\.[0-9]+)?$/) {
        total_age += $7;
        count++;
    }
}
END {
    if (count > 0) {
        average_age = total_age / count;
        printf("Average Age: %.2f\n", average_age);
    } else {
        print("No valid ages found for calculation.");
    }
}' > "$output_file"

echo "Filtered Passengers and Modifed results are stored $output_file"

