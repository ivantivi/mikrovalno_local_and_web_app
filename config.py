from configparser import ConfigParser
import streamlit as st

def config():
    #filename="database.ini", section="postgresql"
    #parser = ConfigParser()
    #parser.read(filename)

    db = {'host': st.secrets.postgresql.host,
    'database': st.secrets.postgresql.database,
    'user': st.secrets.postgresql.user,
    'password': st.secrets.postgresql.password}

    #if parser.has_section(section):
    #    params = parser.items(section)
    #    for param in params:
    #        db[param[0]] = param[1]
    #else:
    #    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

if(__name__=="__main__"):
    print(config())