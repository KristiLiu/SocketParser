import zmq
import json
import time

ctxt = zmq.Context().instance()
in_sock = ctxt.socket(zmq.PULL)
out_sock = ctxt.socket(zmq.PUSH)
out_channel = 'name'


def run(in_addr, out_addr):

    in_sock.connect(in_addr)
    print('connected')
    out_sock.bind(out_addr)
    print("Parser begins listening...")

    try:

            #logic
    except KeyboardInterrupt as e:
        pass


    finally:
        in_sock.close()
        out_sock.close()


if __name__ == "__main__":
  in_addr =
  out_addr =
  run(in_addr, out_addr)
