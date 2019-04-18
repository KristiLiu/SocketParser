import zmq
import json
import time

ctxt = zmq.Context().instance()
in_sock = ctxt.socket(zmq.PULL)
out_sock = ctxt.socket(zmq.PUSH)
out_channel = 'genx5p_parser'


def run(in_addr, out_addr):

    in_sock.connect(in_addr)
    print('connected')
    out_sock.bind(out_addr)
    print("Parser begins listening...")


    try:
        while True:
            raw_bytes= in_sock.recv()

            result_dict = {}
            result_dict['data'] = str(raw_bytes,encoding='ascii')
            print(raw_bytes)


            raw_bytes2= raw_bytes.rstrip()
            raw_bytes3= raw_bytes2.decode("utf-8")

            myList_eachMetric = raw_bytes3.split(",")
            newlist = []
            newlist.append(myList_eachMetric[0])
            time_int= int(myList_eachMetric[12])
            t= time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_int))
            newlist.append(t)
            newlist.append(myList_eachMetric[3])
            newlist.append(myList_eachMetric[4])
            newlist.append(myList_eachMetric[21])
            newlist.append(myList_eachMetric[22])

            result_dict = {'imei':newlist[0], 'send_time':newlist[1] ,'latitude':newlist[2], 'longitude':newlist[3], 'temperature':newlist[4], 'ground_velocity':newlist[5]}

            out_sock.send_json(result_dict)

    except KeyboardInterrupt as e:
        pass


    finally:
        in_sock.close()
        out_sock.close()


if __name__ == "__main__":
  in_addr = 'tcp://192.168.1.24:33000'
  out_addr = 'tcp://192.168.1.24:23000'
  run(in_addr, out_addr)
