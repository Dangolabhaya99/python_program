import sys

import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(notebook):
    conn = None
    sql = """INSERT INTO notebooks VALUES(%s, %s, %s)"""
    values = (notebook.getNID(), notebook.getPages(), notebook.getPrice())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def all():
    pass
def search(nid):
    pass
def edit(notebook):
    pass
def delete(nid):
    pass