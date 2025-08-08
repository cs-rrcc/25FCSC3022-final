'''
CSC 3022 - Security Fundamentals and Databases - Fall 2025
Instructor: Thyago Mota
Student(s):
Description: Final - Taxes Web App
'''

from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, password, authorized):
        self.id = id
        self.name = name
        self.password = password
        self.authorized = authorized

    def __str__(self):
        return f"User(id='{self.id}', name='{self.name}', authorized='{self.authorized}')"
    
class Client:
    def __init__(self, email, name=None, ssn=None, marital_status=None,
                 spouse_name=None, spouse_ssn=None, address=None, filing_jointly=False):
        self.email = email  
        self.name = name
        self.ssn = ssn  # Unique
        self.marital_status = marital_status  
        self.spouse_name = spouse_name
        self.spouse_ssn = spouse_ssn
        self.address = address
        self.filing_jointly = filing_jointly

    def __str__(self):
        return f"Client(email={self.email}, name={self.name}, ssn={self.ssn}, marital_status={self.marital_status}, spouse_name={self.spouse_name},spouse_ssn={self.spouse_ssn}, address={self.address}, filing_jointly={self.filing_jointly})"
    
class ClientYearlyEarning:
    def __init__(self, email, name, year, total_earned):
        self.email = email
        self.name = name
        self.year = year
        self.total_earned = total_earned

    def __str__(self):
        return f"ClientYearlyEarning(email={self.email}, name={self.name}, year={self.year}, total_earned={self.total_earned})"
