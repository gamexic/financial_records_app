import sqlite3

class DatabaseService:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER,
                description TEXT,
                amount REAL,
                type TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def add_record(self, record):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO records (id, description, amount, type)
            VALUES (?, ?, ?, ?)
        ''', (record.id, record.description, record.amount, record.type))
        conn.commit()
        conn.close()

    def get_records(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM records
        ''')
        records = cursor.fetchall()
        conn.close()
        return records

    def get_record(self, id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM records WHERE id=?
        ''', (id,))
        records = cursor.fetchall()
        conn.close()
        return records
    
    def add_money(self, record):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO records (id, description, amount, type)
            VALUES (?, ?, ?, ?)
        ''', (record.id, record.description, record.amount, record.type))
        conn.commit()
        conn.close()
        
    def spend_money(self, record):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO records (id, description, amount, type)
            VALUES (?, ?, ?, ?)
        ''', (record.id, record.description, record.amount, record.type))
        conn.commit()
        conn.close()
