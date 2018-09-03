import psycopg2
import json
import paho.mqtt.client as mqtt
import datetime

 
def connect():
    """ Connect to the PostgreSQL database server """
    
    
        # read connection parameters
    global myConnection
    try:
        # myConnection = psycopg2.connect( host="localhost", user="postgres", password="VVGhrzNAtlPPfOi", dbname="alamsutera") 

        myConnection = psycopg2.connect( host="localhost", user="alamsutera", password="alamsutera9545", dbname="alamsutera") 

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
        # create a new cursor
        # execute the INSERT statement
        cur.execute(sql, (unique_key, guard_id, shift_id, datetime.datetime.today(),cluster_id, longitude, latitude, acc))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        myConnection.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
 
    return vendor_id

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/api/cluster")

def on_message(client, userdata, msg):
    dataJson = json.loads(msg.payload)
    # for key, value in dataJson.items():
    #     print key, value
    insert_data(dataJson['unique_key'], dataJson['username'], dataJson['shift_id'], dataJson['cluster_code'], dataJson['lat'], dataJson['lng'], dataJson['acc'])
 
if __name__ == '__main__':
    myConnection = None
    connect()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("209.97.168.161", 1883, 60)
    client.loop_forever()


     
