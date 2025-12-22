import csv
import pymysql

# 1. Connect to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Dhrubo@09122003',
    database='sakila',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 2. Create Rental table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Rental (
    rental_id INT PRIMARY KEY,
    rental_date DATETIME,
    inventory_id INT,
    customer_id INT,
    return_date DATETIME,
    staff_id INT,
    last_update DATETIME
)
"""

# 3. Insert query
insert_sql = """
REPLACE INTO Rental (
    rental_id, rental_date, inventory_id, customer_id,
    return_date, staff_id, last_update
) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# 4. Chunked insert function
def insert_in_chunks(reader, chunk_size=1000):
    batch = []
    for row in reader:
        cleaned = [col.strip('"') if col else None for col in row]
        batch.append(tuple(cleaned))
        if len(batch) >= chunk_size:
            with connection.cursor() as cursor:
                cursor.executemany(insert_sql, batch)
                connection.commit()
            print(f"✅ Inserted {len(batch)} rows...")
            batch.clear()
    if batch:
        with connection.cursor() as cursor:
            cursor.executemany(insert_sql, batch)
            connection.commit()
        print(f"✅ Inserted final {len(batch)} rows.")

# 5. Run the import
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)
            connection.commit()

        with open('rental.csv', mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Skip header
            insert_in_chunks(reader)

        print("🎉 All rental records imported successfully!")

except Exception as e:
    print(f"⚠️ Error: {e}")
