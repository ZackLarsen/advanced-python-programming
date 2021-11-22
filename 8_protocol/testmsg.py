# testdecode.py
#
# Connect to this and it will send you a few messages to decode.

import time
import random

msg1 = b'ChatMessage\r\n58\r\n{"sequence": 1, "playerid": "Dave", "text": "Hello World"}'
msg2 = b'PlayerUpdate\r\n54\r\n{"sequence": 2, "playerid": "Paula", "x": 23, "y": 41}'

def send_message(sock, msg):
    # Send the message is small fragments with time delay.  Goal is to 
    # force fragmentation on receiver.
    while msg:
        nsent = sock.send(msg[:random.randint(1,10)])
        time.sleep(0.001)
        msg = msg[nsent:]
    
def main():
    from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.bind(('', 19000))
    sock.listen(1)
    print('Connection to ("localhost", 19000) to get messages')
    while True:
        client, addr = sock.accept()
        try:
            send_message(client, msg1)
            send_message(client, msg2)
        except OSError as e:
            pass
        client.close()

if __name__ == '__main__':
    main()

