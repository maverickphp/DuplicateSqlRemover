# SQL Duplicate Line Remover

This Python code reads a SQL file, removes duplicate lines, and saves the unique lines to a new SQL file.

<h3>Prerequisites:</h3>
Python 3.x

<h3>Usage:</h3>

1. Save the input SQL file as input.sql in the same directory as the Dplsqlrmv.py file.
2. Run the Python script using the following command:

```sh
python Dplsqlrmv.py
```

3. The unique lines will be saved in a new SQL file named output.sql.

<h3>How it Works:</h3>
1. The script reads the lines of the input SQL file into a list.
2. An empty set is created to store unique lines.
3. The script loops over each line in the list, strips any leading/trailing whitespace from the line, and checks if the line is not empty and not already in the set.
4. If the line is unique, it is added to the set.
5. Finally, the unique lines are written to the output SQL file.

<h3>Limitations</h3>

This script only removes exact duplicate lines. If two lines have the same meaning but different formatting or whitespace, they will be considered different and both will be included in the output file.

<h3>License</h3>
This code is licensed under the MIT License.
