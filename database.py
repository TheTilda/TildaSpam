import sqlite3
from os import path


def get_script_dir():
    abs_path = path.abspath(__file__) # полный путь к файлу скрипта
    return path.dirname(abs_path)

DB_FILE = get_script_dir() + path.sep + 'base.db'
#Коннект к базе
db = sqlite3.connect(DB_FILE)
sql = db.cursor()
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS account (
    name TEXT,
    time BIGINT
)""")

db.commit()