import psycopg2
from config import config

def get_data(size = "100"):
    conn = None
    size = str(size)
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #Dohvati sve
        #cur.execute("SELECT * from Sensor_data")
        #Dohvati zadnjih 100(size)
        command = "SELECT * FROM Sensor_data ORDER BY id DESC LIMIT %s"
        cur.execute(command, (size,))
        data_list = cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return data_list

