'''
CSC 3022 - Security Fundamentals and Databases - Fall 2025
Instructor: Thyago Mota
Student(s):
Description: Final - Taxes Web App
'''

from app import app, get_conn
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import SignUpForm, LoginForm
from app.models import User, Client, ClientYearlyEarning
# import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data == form.password_confirm.data:
            # consider salting and hashing passwords using bcrypt
            password = form.password.data
            conn = get_conn(read_only=False)
            cursor = conn.cursor()
            try:
                sql = f"INSERT INTO Users (Id, Name, Password) VALUES ('{form.id.data}', '{form.name.data}', '{password}')"
                cursor.execute(sql)
                conn.commit()
            except Exception as ex: 
                return f'<p>❌ Error: {ex}</p>'
            return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        conn = get_conn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM Users WHERE id = '{form.id.data}'"
        cursor.execute(sql)
        try:
            result = cursor.fetchone()
            if result: 
                user = User(*result)
                if user.authorized and form.password.data == user.password:
                    login_user(user)
                    if current_user.is_authenticated: 
                        return redirect(url_for('list_clients'))
            return f'<p>❌ Error: Unauthorized!</p>'
        except Exception as ex: 
                return f'<p>❌ Error: {ex}</p>'
    return render_template('login.html', form=form)

@login_required
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/clients')
@login_required
def list_clients():
    try: 
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * FROM clients"
        cursor.execute(sql)
        results = cursor.fetchall()
        clients = []
        for result in results: 
            client = Client(email=result[0], name=result[1], ssn=result[2], marital_status=result[3], spouse_name=result[4], spouse_ssn=result[5], address=result[6], filing_jointly=result[7])
            clients.append(client)
        return render_template('clients.html', clients=clients)
    except Exception as ex: 
        return f'<p>❌ Error: {ex}</p>'

@app.route('/clients/<email>')
@login_required
def client_yearly_earnings(email):
    try: 
        conn = get_conn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM ClientYearlyEarnings WHERE Email = '{email}'"
        cursor.execute(sql)
        results = cursor.fetchall()
        client_yearly_earnings = []
        for result in results:
            client_yearly_earning = ClientYearlyEarning(*result)
            client_yearly_earnings.append(client_yearly_earning)
        return render_template('client_yearly_earnings.html', client_yearly_earnings=client_yearly_earnings)
    except Exception as ex: 
        return f'<p>❌ Error: {ex}</p>'