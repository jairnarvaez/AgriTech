import socket
import time
from random import randint

def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  # replace with the server's IP address
    server_port = 8001  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    while True:
        # input message and send it to the server
        tipo = [' potacio', ' fosforo', ' nitrogeno'][randint(0,2)]
        msg = '3'+str(randint(0, 100))
#       msg = input('Number: ')
        #msg = '1'
        print(f"Send: {msg}")

        client.send(msg.encode("utf-8")[:1024])

        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break

        time.sleep(1)

        #print(f"Received: {response}")
        

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

print("Client start")
run_client()
