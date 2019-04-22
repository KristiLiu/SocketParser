import zmq
import json
import ppinrt

import mysql.connector
from mysql.connector import Error

def consumer():

    #create a zmq object instance to pull incoming json data
    ctxt= zmq.Context()
    consumer_receiver_sock= ctxt.socket(zmq.PULL)
    consumer_receiver_sock.connect("tcp://")
    print("connecting to port")

    while True:
        JSonString =consumer_receiver_sock.recv_json()
        pprint.pprint(JSonString)

        #Deconstruct the json string and save them into variables
        imei = JSonString["imei"]
        temperature = JSonString["temperature"]
        ground_velocity = JSonString["ground_velocity"]
        latitude = JSonString["latitude"]
        longitude = JSonString["longitude"]
        sendtime = JSonString["send_time"]

        try:
            #connect to local database in workbench
            connection = mysql.connector.connect(host='localhost',
                             database='testdb',
                             user='root',
                             password='password')

            #Query script to insert into the readings table in the testdb
            sqlInsertQuery = """INSERT INTO 'readings_table'
            VALUES (imei, temperature, ground_velocity, latitude, longitude, sendtime);"""

            if connection.is_connected():

                #Get server version info
                db_Info = connection.get_server_info()
                print("Connected to MySQL database, DB Info: ",db_Info)

                #Create cursor object instance
                cursor = connection.cursor()

                #Execute insert query
                result = cursor.execute(sqlInsertQuery)

                #Commit changes to database
                connection.commit()
                print("Record inserted into table")

        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

consumer()
