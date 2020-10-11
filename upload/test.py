import sqlite3, os
from sqlite3 import Error

def query_db():
    conn = None
    my_fir_no = 420
    try:
        conn = sqlite3.connect('../copsdb.sqlite3')
        cursor = conn.cursor()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        cursor.execute(f'SELECT name FROM Criminal WHERE fir_no = {my_fir_no}')
        print(cursor.fetchone())
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
