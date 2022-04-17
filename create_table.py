import psycopg2
from config import config


conn = None
try:
    params = config()
    print("Connecting to the PostgreSQL database")
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
       
    cur.execute("""
        CREATE TABLE Sensor_Data(
            ID SERIAL PRIMARY KEY NOT NULL,
            TEMPERATURE REAL,
            PRESSURE REAL,
            HUMIDITY REAL,
            ALTITUDE REAL,
            TIME TEXT
        )
    """)
    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("Database cennection closed")
