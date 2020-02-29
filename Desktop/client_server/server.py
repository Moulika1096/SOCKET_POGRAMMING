import socket

def strip_cmd(cmd,data):
    data_without_cmd = data[0 + len(cmd):len(data)].strip()
    return data_without_cmd

def cmd_control(client_sock, data):
    n = data.find("say")
    if (n == 0):
        data_without_cmd = strip_cmd("say",data)
        print data_without_cmd
        client_sock.send(data_without_cmd+"\n") # if client sends say hello, we print hello
    else:
        n = data.find("eval")
        if (n == 0):
            expr = strip_cmd("eval", data)
            print expr
            out = eval(expr)
            client_sock.send(expr+" = "+str(out)+"\n")  # if client sends eval 2=3, send 2+3 = 5
        else:
            client_sock.send("unknown command")


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "socket created"
  
port = 9090
#Bind to empty ip address, means 0.0.0.0, meaning bindig to current ip and localhost ip address 127.0.0.1
s.bind(('', port))         
print "Bound to port %s" %(port) 

# Listen for incoming traffic
s.listen(5)
print "started listening"
  
# loop until error is thrown

while True:
    try:
        # call to accept api blocks until client connects
        client_sock, addr = s.accept()      
        print 'Connection received from', addr 
        while True:
            data = client_sock.recv(1024)
            n = data.find("\n")
            if(n > 0):
                print "Data received from client = "+data
                cmd_control(client_sock,data.strip())
            else:
                client_sock.send("unknown command")

    except Exception as e:
        print(e)
        # Close the connection with the client
        client_sock.close() 
