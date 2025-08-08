'''
CSC 3022 - Security Fundamentals and Databases - Fall 2025
Instructor: Thyago Mota
Student(s):
Description: Final - Port Scanner
Disclaimer: 
    
    The code and instructions provided are intended solely for educational purposes. They are designed to help learners understand security concepts and practices in a controlled, academic environment.

    Do not use this code or any related techniques to perform penetration testing or security assessments on production systems, live environments, or systems under active development without proper authorization.

    The instructor and course facilitators are not responsible for any misuse of the materials or any consequences resulting from unauthorized testing or deployment.
    
'''

import socket

# Common database ports
DATABASE_PORTS = {
    "MySQL": 3306,
    "PostgreSQL": 5432,
    "Oracle": 1521,
    "SQL Server": 1433
}

def check_port(host, port, timeout=2):
    """Check if a port is open on the given host."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def scan_database_ports(host):
    print(f"Scanning {host} for open database ports...\n")
    for db_name, port in DATABASE_PORTS.items():
        if check_port(host, port):
            print(f"✅ {db_name} port {port} is open and accepting connections.")
        else:
            print(f"❌ {db_name} port {port} is closed or unreachable.")

if __name__ == "__main__":
    target_host = input("Enter the target host (e.g., example.com or IP): ")
    scan_database_ports(target_host)
