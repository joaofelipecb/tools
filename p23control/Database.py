import psycopg2
import p17data.Config

link = None

def connect(profile='default'):
    global link
    dbms = p17data.Config.database[profile]['dbms']
    host = p17data.Config.database[profile]['host']
    user = p17data.Config.database[profile]['user']
    password = p17data.Config.database[profile]['password']
    database = p17data.Config.database[profile]['database']
    link = psycopg2.connect(host=host, database=database, user=user, password=password)
    return True

connect()

def query(query):
    global link
    cur = link.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result

