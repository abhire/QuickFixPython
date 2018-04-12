import socket
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('localhost', 10000)
eprint('starting up on %s port %s' % server_address)
sock.bind(server_address)




# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    eprint('waiting for a connection')
    connection, client_address = sock.accept()


    try:
        eprint('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            eprint('received "%s"' % data)
            if data:
                eprint('sending data back to the client')
                connection.sendall(data)
            else:
                eprint('no more data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()



