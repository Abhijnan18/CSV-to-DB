import pandas as pd
import mysql.connector

# Function to create a MySQL connection and cursor
def create_mysql_connection():
    connection = mysql.connector.connect(
        host='your_mysql_host',
        user='your_mysql_user',
        password='your_mysql_password',
        database='studentdetials'
    )
    cursor = connection.cursor()
    return connection, cursor

# Read data from CSV file starting from row 4 with explicit column names
csv_file_path = 'your_csv_file.csv'
df = pd.read_csv(csv_file_path, skiprows=3, usecols=['Students Name', 'IA I', 'IA 2'])

# Replace 'AB' with NULL in IA marks columns
df['IA I'].replace('AB', None, inplace=True)
df['IA 2'].replace('AB', None, inplace=True)

# Convert columns to numeric (if not already) and replace NaN with 0
df['IA I'] = pd.to_numeric(df['IA I'], errors='coerce').fillna(0)
df['IA 2'] = pd.to_numeric(df['IA 2'], errors='coerce').fillna(0)

# Establish MySQL connection
try:
    connection, cursor = create_mysql_connection()

    # Iterate through the DataFrame and insert data into the MySQL database
    for index, row in df.iterrows():
        student_name = row['Students Name']
        ia1_score = row['IA I']
        ia2_score = row['IA 2']

        # MySQL query to insert data into the table (assuming the table is named 'student_marks')
        insert_query = f"INSERT INTO student_marks (student_name, ia1_score, ia2_score) VALUES ('{student_name}', {ia1_score}, {ia2_score})"

        # Execute the query
        cursor.execute(insert_query)

    # Commit the changes
    connection.commit()
    print("Data inserted into MySQL database successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection in the finally block to ensure it's closed even if an exception occurs
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
