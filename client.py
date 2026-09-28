#import socket as s
#client_socket=s.socket(s.AF_INET,s.SOCK_STREAM)
#server_addr=("localhost",3000)
#client_socket.connect(server_addr)
#try:
    #print("connected to server:",server_addr)
    #message=input("enter message>>")
    #client_socket.sendall(message.encode('utf-8'))
    #server_data=client_socket.recv(1024).decode()
    #if server_data:
        #print("message recieved from server>>",server_data)
        #message=input("enter the message>>")
        #client_socket.sendall(message.encode('utf-8'))
    #else:
        print("no response recieved from server")
#finally:
    print("closing the connection")
    client_socket.close()
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='
')  # Print timer in same line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if _name_ == "_main_":
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid integer for the time.")