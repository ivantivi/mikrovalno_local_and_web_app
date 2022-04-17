import psycopg2
from config import config

def send_data(data, time):
    """
    Send data to SQL server
    :param list data: Data should contain [temperature, pressure, humidity, altitude]
    :param str time: Time string
    """
    parameters = (data[0], data[1], data[2], data[3], time)
    insert = ("INSERT INTO Sensor_data (temperature, pressure, humidity, altitude, time) VALUES %s")
    conn = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
            
        cur.execute(insert, (parameters,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database cennection closed")
