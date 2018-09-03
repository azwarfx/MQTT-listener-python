import psycopg2
import json
import paho.mqtt.client as mqtt
import datetime

 
def connect():
    """ Connect to the PostgreSQL database server """
    
    
        # read connection parameters
    global myConnection
    try:
        myConnection = psycopg2.connect( host="localhost", user="postgres", password="VVGhrzNAtlPPfOi", dbname="alamsutera") 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
 
        # create a cursor
        # cur = myConnection.cursor()
        
         # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        # db_version = cur.fetchone()
        # print(db_version)
       
     # close the communication with the PostgreSQL
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
        # if conn is not None:
        #     conn.close()
        #     print('Database connection closed.')

def insert_data(unique_key, guard_id, shift_id,cluster_id, latitude, longitude, acc):
    """ insert a new vendor into the vendors table """
    global myConnection
    sql = """INSERT INTO temp(unique_key, guard_id,shift_id, created_at, cluster_id, longitude, latitude, accuracy)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
    vendor_id = None
    try:
        # myConnection = psycopg2.connect( host="localhost", user="postgres", password="VVGhrzNAtlPPfOi", dbname="alamsutera")
        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')

        # create a cursor
        cur = myConnection.cursor()
     
