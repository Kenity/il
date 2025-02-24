import sqlite3
from MVP.cogs.find_DataBase import FindDB

class AdminCRUD:
    def __init__(self, db_path = FindDB().find_database_path()):
        self.db_path = db_path

    def get_student(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM students')
        result=cursor.fetchall()
        connection.close()
        return result


    def get_teachers(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM teachers')
        result=cursor.fetchall()
        connection.close()
        return result

    def get_courses(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM courses')
        result=cursor.fetchall()
        connection.close()
        return result

    def get_enrollments(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM enrollments')
        result=cursor.fetchall()
        connection.close()
        return

    def get_user(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM users')
        result=cursor.fetchall()
        connection.close()
        return result