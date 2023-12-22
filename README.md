# CSV-to-DB Project

## Overview

The CSV-to-DB project is designed to read student data from a CSV file and insert it into a MySQL database. This README provides a guide on setting up the database, creating a table, and running the Python script to insert data.

## Project Structure

- `csv-to-db.py`: Python script to read CSV data and insert it into the MySQL database.
- `your_csv_file.csv`: Sample CSV file containing student data.

## Setup

### 1. Create Database

```sql
CREATE DATABASE studentdetials;
USE studentdetials;
```

### 2. Create Table

```sql
CREATE TABLE student_marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    ia1_score INT,
    ia2_score INT
);
```

## Running the Python Script

1. Install the required Python packages:

    ```bash
    pip install pandas mysql-connector-python
    ```

2. Update script with your MySQL credentials and CSV file path.

3. Run the script:

    ```bash
    python3 csv-to-db.py
    ```

## Viewing Data

- Use a MySQL client (e.g., MySQL Workbench) or command-line interface to view data in the `student_marks` table.

### MySQL Workbench

1. Open MySQL Workbench.
2. Connect to your MySQL server.
3. Select the `studentdetials` database.
4. Navigate to the `student_marks` table.
5. Right-click and choose "Select Rows - Limit 1000" to view data.

### MySQL Command-Line Interface

```bash
mysql -u your_username -p -h localhost studentdetials
```

Enter your password, then run:

```sql
SELECT * FROM student_marks;
```

## Notes

- Replace placeholders (`your_csv_file.csv`, `your_username`, etc.) with actual details.
- Do not include sensitive information in this `README.md` file.

# Screen-Shot of the Result

![Screenshot 2023-12-22 at 4 16 27 PM](https://github.com/Abhijnan18/CSV-to-DB/assets/114734468/7cd91b6c-134c-4a97-980b-d54af074490a)



