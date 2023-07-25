
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    DB = 'report_schema'
    def __init__(self, user_data):
        self.id = user_data['id']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email'] 
        self.api_number = user_data['api_number']
        self.password = user_data['password']
        self.created_at = user_data['created_at']
        self.updated_at = user_data['updated_at']

    @classmethod
    def save_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, api_number, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(api_number)s, %(password)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_user_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(user_id)s"
        data = {
            'user_id': user_id
        }
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])  # Make sure the returned user object contains the required attributes
        return None

    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.DB).query_db(query,user)
        if len(results) >= 1:
            flash("Email already Registered, Go to Login.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email","register")
            is_valid=False
        if len(user['first_name']) < 1:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(user['last_name']) < 1:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match","register")
        return is_valid
    

