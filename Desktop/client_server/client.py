import sys
import socket
s = socket.socket()
port = 9090 #default if nothing specified from command line
ip = '127.0.0.1'
if (len(sys.argv)>2):
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print "using default ip and port, since no arguments are specified"

# connect to the server on local computer
try:
    s.connect((ip, port))
    while True:
        command = raw_input("Enter command: ")
        if (command == "quit"):
            break
        print "entered "+command+" \n"
        s.send(command+"\n")
        print "Received from server : "+s.recv(1024)

except Exception as e:
    print "Failed to connect to "+ip+":"+str(port)
    print e
s.close()
