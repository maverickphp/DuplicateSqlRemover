# Open the input SQL file for reading
with open('/path/to/input.sql', 'r') as f:
    # Read the lines into a list
    lines = f.readlines()

# Create an empty set to store unique lines
unique_lines = set()

# Loop over each line in the list
for line in lines:
    # Strip any leading/trailing whitespace from the line
    line = line.strip()

    # Check if the line is not empty and not already in the set
    if line and line not in unique_lines:
        # If the line is unique, add it to the set
        unique_lines.add(line)

# Open the output SQL file for writing
with open('output.sql', 'w') as f:
    # Write the unique lines to the output file
    for line in unique_lines:
        f.write(line + '\n')
