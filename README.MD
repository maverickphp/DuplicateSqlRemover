# SQL Duplicate Line Remover

This Python code reads a SQL file, removes duplicate lines, and saves the unique lines to a new SQL file.

<h3>Prerequisites</h3>
Python 3.x
Usage
Save the input SQL file as input.sql in the same directory as the sql_duplicate_line_remover.py file.

Run the Python script using the following command:

Copy code
python sql_duplicate_line_remover.py
The unique lines will be saved in a new SQL file named output.sql.

How it Works
The script reads the lines of the input SQL file into a list.
An empty set is created to store unique lines.
The script loops over each line in the list, strips any leading/trailing whitespace from the line, and checks if the line is not empty and not already in the set.
If the line is unique, it is added to the set.
Finally, the unique lines are written to the output SQL file.
Example
Suppose we have the following SQL file named input.sql:

sql
Copy code
SELECT *
FROM employees
WHERE salary > 50000;
SELECT *
FROM employees
WHERE salary > 50000;
SELECT *
FROM departments;
Running the script using the command python sql_duplicate_line_remover.py will produce a new SQL file named output.sql with the following contents:

sql
Copy code
SELECT *
FROM employees
WHERE salary > 50000;
SELECT *
FROM departments;
Limitations
This script only removes exact duplicate lines. If two lines have the same meaning but different formatting or whitespace, they will be considered different and both will be included in the output file.
License
This code is licensed under the MIT License.
