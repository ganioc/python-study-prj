import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5678")

socket.send(b"Load request")

message = socket.recv()
print("Received reply %s [ %s ]" % ('request', message))


