import sqlite3

connector = sqlite3.connect('parking_martynas.db')
cursor = connector.cursor()

def create_tables(connector=connector, cursor=cursor):
    queries = [
'''
CREATE TABLE IF NOT EXISTS car(
    id INTEGER PRIMARY  KEY AUTOINCREMENT,
    plate VARCHAR(15) NOT NULL
);
''',
'''
CREATE TABLE IF NOT EXISTS tariff(
    id INTEGER PRIMARY  KEY AUTOINCREMENT,
    duration_hour INTEGER,
    price_per_hour DECIMAL(18, 2) DEFAULT 0
);
''',
''' 
CREATE TABLE IF NOT EXISTS parking(
    id INTEGER PRIMARY  KEY AUTOINCREMENT,
    arrival DATETIME NOT NULL,
    departure DATETIME,
    car_id INTEGER REFERENCES car(id),
    tariff_id INTEGER REFERENCES tariff(id),
    total_price DECIMAL(18,2) DEFAULT 0
);
''',
    ]
    with connector:
        for query in queries:
            cursor.execute(query)
create_tables()