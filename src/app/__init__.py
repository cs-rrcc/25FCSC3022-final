'''
CSC 3022 - Security Fundamentals and Databases - Fall 2025
Instructor: Thyago Mota
Student(s):
Description: Final - Taxes Web App
'''

from flask import Flask, g
import mysql.connector
from configparser import ConfigParser
from app.models import User

def get_conn(read_only=True): 
    with app.app_context():
        if 'conn' not in g:
            parser = ConfigParser()
            parser.read('db.ini')
            db_config = {
                'host': parser.get('mysql', 'host'),
                'port': parser.getint('mysql', 'port', fallback=3306),
                'database': parser.get('mysql', 'database')
            }
            if read_only:
                db_config['user'] = parser.get('mysql_read', 'user')
                db_config['password'] = parser.get('mysql_read', 'password')
            else:
                db_config['user'] = parser.get('mysql_write', 'user')
                db_config['password'] = parser.get('mysql_write', 'password')
            g.conn = mysql.connector.connect(**db_config)
        return g.conn

app = Flask("Taxes App")

# note that CSRF had to be disable for SQLMap to run!
app.config['WTF_CSRF_ENABLED'] = False

# consider using an ENVIRONMENT VARIABLE to improve security
app.secret_key = 'you-will-never-guess'

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        conn = get_conn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM Users WHERE id = '{id}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result: 
            return User(*result)
    except: 
        pass
    return None

from app import routes
