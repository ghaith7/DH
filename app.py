import socket
from client import Client


print ( "to use the chat app you must first enter your coordintes")
login = input("enter your pseudo : ")
client = Client(login=login)
HOST = '192.168.100.247'  # The server's hostname or IP address
PORT = 8000        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall( ("""C
    {}
    """.format(login)).encode()  )
    data = s.recv(1024)
    print('Received : ', repr(data))
    print("enter the name of the user you want to talk to")
    bob=input()
    while(True):
        msg=input(login+" : ")
        s.sendall( ("""S
        {}:{}:{}""".format(login,bob,msg)).encode() )
        data = s.recv(1024)
        s.sendall(("""R
        {}:{}""".format(login,bob,msg)).encode())
        data = s.recv(1024)
        print('Received : ', str(repr(data)))