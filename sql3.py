import csv
import pymysql

# 1. Connect to MySQL using your credentials
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Dhrubo@09122003',
    database='sakila',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 2. Create the Actor table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Actor (
    actor_id INT PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    last_update DATETIME
)
"""

# 3. Insert query using REPLACE to handle duplicates
insert_sql = """
REPLACE INTO Actor (actor_id, first_name, last_name, last_update)
VALUES (%s, %s, %s, %s)
"""

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)
            connection.commit()

        with open('actor.csv', mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Skip header row
            rows = []
            for row in reader:
                cleaned = [col.strip('"') if col else None for col in row]
                rows.append(tuple(cleaned))

        with connection.cursor() as cursor:
            cursor.executemany(insert_sql, rows)
            connection.commit()
            print(f"✅ Successfully inserted {len(rows)} rows into the Actor table.")

except Exception as e:
    print(f"⚠️ Error during import: {e}")
