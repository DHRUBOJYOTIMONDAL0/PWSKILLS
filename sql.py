import csv
import pymysql

# 1. Connect to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Dhrubo@09122003',
    database='PW_SKILLS',
    charset='utf8mb4',  # Ensure UTF-8 support
    cursorclass=pymysql.cursors.DictCursor
)

# 2. Create table (if not exists)
create_table_sql = """
CREATE TABLE IF NOT EXISTS World_City (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    CountryCode VARCHAR(10),
    District VARCHAR(255),
    Population INT
)
"""

# 3. Read and insert CSV data
insert_sql = """
INSERT INTO World_City (ID, Name, CountryCode, District, Population)
VALUES (%s, %s, %s, %s, %s)
"""

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)
            connection.commit()

        with open('City.csv', mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Skip header
            rows = []
            for row in reader:
                # Clean values: remove surrounding quotes
                cleaned = [col.strip('"') for col in row]
                rows.append(tuple(cleaned))

            with connection.cursor() as cursor:
                cursor.executemany(insert_sql, rows)
                connection.commit()
                print(f"✅ Inserted {len(rows)} rows successfully.")

except Exception as e:
    print(f"⚠️ Error: {e}")
