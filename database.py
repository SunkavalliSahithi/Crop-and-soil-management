import sqlite3

def create_connection():
    conn = sqlite3.connect('crop_soil_management.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        planting_date TEXT,
        harvest_date TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS soil (
        id INTEGER PRIMARY KEY,
        crop_id INTEGER,
        pH REAL,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL,
        FOREIGN KEY(crop_id) REFERENCES crops(id)
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_crop(name, planting_date, harvest_date):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO crops (name, planting_date, harvest_date)
    VALUES (?, ?, ?)
    ''', (name, planting_date, harvest_date))
    
    conn.commit()
    conn.close()

def insert_soil(crop_id, pH, nitrogen, phosphorus, potassium):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO soil (crop_id, pH, nitrogen, phosphorus, potassium)
    VALUES (?, ?, ?, ?, ?)
    ''', (crop_id, pH, nitrogen, phosphorus, potassium))
    
    conn.commit()
    conn.close()

def get_crops():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM crops')
    crops = cursor.fetchall()
    
    conn.close()
    return crops

def get_soil_for_crop(crop_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM soil WHERE crop_id = ?', (crop_id,))
    soil_data = cursor.fetchall()
    
    conn.close()
    return soil_data
