import sqlite3

def create_conn(database):
    conn = sqlite3.connect(database)
    if conn:
        print("connection to {} successful".format(database))
        return conn
    else:
        print("connection to {} unsuccessful".format(database))
        exit(-1)
    
def close_conn(conn):
    if conn:
        print("closing connection to database")
        conn.close()
    else:
        print("error no connection found")


def create_database(database):
    conn = create_conn(database)
    conn.commit()
    print("created {} successful".format(database))
    close_conn(conn)


def add_button_table_to_db(database,tablename):
    conn = create_conn(database)
    c = conn.cursor()
    query = """CREATE TABLE {}(timestamp DATETIME, action INTEGER)""".format(tablename)
    c.execute(query)
    conn.commit
    print("created table: {}".format(tablename))
    close_conn(conn)


def add_DHT_table_to_db(database,tablename):
    conn = create_conn(database)
    c = conn.cursor()
    query = """CREATE TABLE {}(timestamp DATETIME, Temp FLOAT, humid FLOAT)""".format(tablename)
    c.execute(query)
    conn.commit
    print("created table: {}".format(tablename))
    close_conn(conn)

def add_relay_table_to_db(database,tablename):
    conn = create_conn(database)
    c = conn.cursor()
    query = """CREATE TABLE {}(timestamp DATETIME, msg TEXT)""".format(tablename)
    c.execute(query)
    conn.commit
    print("created table: {}".format(tablename))
    close_conn(conn)

def delete_table(database,tablename):
    conn = create_conn(database)
    c = conn.cursor()
    query = """DROP TABLE {}""".format(tablename)
    c.execute(query)
    conn.commit
    print("deleted table: {}".format(tablename))
    close_conn(conn)


def insert_button_or_relay_to_db(database,tablename,value1,value2):
    conn = create_conn(database)
    c = conn.cursor()
    query = """INSERT INTO {} VALUES(:value1,:value2)""".format(tablename)
    c.execute(query,{"value1":value1,"value2":value2})
    conn.commit()
    print("inserted data into table: {} successfully".format(tablename))
    close_conn(conn)

def insert_DHT_to_db(database,tablename,value1,value2,value3):
    conn = create_conn(database)
    c = conn.cursor()
    query = """INSERT INTO {} VALUES(:value1,:value2,:value3)""".format(tablename)
    c.execute(query,{"value1":value1,"value2":value2,"value3":value3})
    conn.commit()
    print("inserted data into table: {} successfully".format(tablename))
    close_conn(conn)

def get_data_from_table(database,tablename):
    conn = create_conn(database)
    c = conn.cursor()
    query = """SELECT rowid,* FROM {}""".format(tablename)
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    close_conn(conn)


def delete_row_from_db(database,tablename,rowid):
    conn = create_conn(database)
    c = conn.cursor()
    query = """DELETE FROM {} where rowid=:rowid""".format(tablename)
    try:
        c.execute(query,{"rowid":rowid})
        conn.commit
        print("row {} deleted".format(rowid))
    except sqlite3.Error as error:
            print("Failed to delete row ",error)
    finally:
        close_conn(conn)


database = "SmartHeat.db"
button_table = "sensor_button"
DHT_table = "sensor_DHT"
relay_table = "sensor_relay"


# first run
# create_database(database)
# add_button_table_to_db(database,button_table)
# add_DHT_table_to_db(database,DHT_table)
# add_relay_table_to_db(database,relay_table)
