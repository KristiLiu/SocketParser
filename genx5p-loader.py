import zmq
import json
import pprint

def consumer():
    ctxt= zmq.Context()
    consumer_receiver_sock= ctxt.socket(zmq.PULL)
    consumer_receiver_sock.connect("tcp://192.168.1.124:43000")
    print("connecting to port")
    while True:
        JSonString =consumer_receiver_sock.recv_json()
        # data2 = json.dumps(JSonString)
        pprint.pprint(JSonString)

        #dictObj = json.loads(JSonString)
        #pprint.pprint(dictObj)
        #console.log(dictObj)
consumer()
