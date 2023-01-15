import socket 
from threading import Thread

#HOST = '0.0.0.0'
HOST = socket.gethostbyname('socket-server_dns_name')
PORT = 5051  

def loop_server():
    client = [] # Массив где храним адреса клиентов

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind ((HOST,PORT))
    while True:
        data,addr = sock.recvfrom(1024)
        print (addr[0], addr[1], data.decode('utf-8'))
        if  addr not in client: 
            client.append(addr)# Если такого клиента нету, то добавить
            print (client)
        for clients in client:
            if clients == addr: 
                continue # Не отправлять данные клиенту, который их прислал
            sock.sendto(data,clients)
            print(sock.sendto(data,clients))

if __name__ == '__main__':
    # start thread with loop
    Thread(target=loop_server, args=(), name='loop_server', daemon=True).start()
    try:
        input("Start Server. Enter any key for exit. ")
    except EOFError:
        print("Exception handled")