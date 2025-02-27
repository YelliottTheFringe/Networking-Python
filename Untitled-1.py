#Server-basic
import socket as sk
from random import randint
server = sk.socket(sk.AF_INET,sk.SOCK_STREAM) # making a socket, AF_INET means wifi and SOCK_STREAM means TCP protocall (don't change it)
v=randint(1,40) #ignore this until later
server.bind(('',(12000+v)))# binds a port to ' ' (which means localhost) and port 12,000 + the random number from earlier. Note that all this is sandwiched between two sets of ()
print(v+12000) # print port number
server.listen(4) # Allow connections
print("going") # Check to make sure nothing failed
while True: # start loop
    v,c =server.accept() #accept connections
    try:
        v.send("cheese".encode()) # sends message through TCP protocall
        print("connected",v) #either fails before this or prints this message. Either way, you get text
    except:
        server.close #kills server on a failiture
    server.close() # kills server anyway I have no idea why this is here
    break