import psycopg2
import p17data.Config

def connect(profile='default'):
    dbms = p17data.Config.database[profile]['dbms']
    host = p17data.Config.database[profile]['host']
    user = p17data.Config.database[profile]['user']
    password = p17data.Config.database[profile]['password']
    database = p17data.Config.database[profile]['database']
    con = psycopg2.connect(host=host, database=database, user=user, password=password)
    return True


