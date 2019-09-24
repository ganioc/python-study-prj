import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5678")

# Socket 

while True:
    message = socket.recv()
    print("Received request: %s" % message)

    time.sleep(2)

    socket.send_string(str(random.random()))



