import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="31356mysql29@",
        database="BackendExam"
    )

    cur = conn.cursor()

    country_name = input("Enter Country name to find: ")

   
    cur.execute('''SELECT country_id
                   FROM countries
                   WHERE country_name = %s''', (country_name,))
    country_id_row = cur.fetchone()

    
    if not country_id_row:
        print("Country not found.")
    else:
        country_id = country_id_row[0]

        
        cur.execute('''SELECT location_id, street_address, city, state_province
                       FROM locations
                       WHERE country_id = %s''', (country_id,))
        rows = cur.fetchall()

        
        for row in rows:
            print("Country:", country_name) 
            print("Location ID:", row[0])
            print("Street Address:", row[1])
            print("City:", row[2])
            print("State/Province:", row[3])
            print()

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    # Close cursor and connection
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
