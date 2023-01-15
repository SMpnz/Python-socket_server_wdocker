import socket,threading
from threading import Thread

#HOST = '192.168.7.66'
HOST = socket.gethostbyname('socket-server_dns_name')
PORT = 5051
PORTCLI = 9999

def loop_client():
    def read_sok():
        while True:
            data = sor.recv(1024)
            print(data.decode('utf-8'))
    server = HOST, PORT  # Данные сервера
    print("Клиент запущен. Пишите сообщения. Выход:F2")
    alias = "Cl_duty" # Вводим наш псевдоним
    sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sor.bind(('', PORTCLI)) # Задаем сокет как клиент
    sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении
    potok = threading.Thread(target= read_sok)
    potok.start()
    while True:
        messagetosend = input()
        sor.sendto(('['+alias+ ']'+messagetosend).encode('utf-8'), server)

if __name__ == '__main__':
    Thread(target=loop_client, args=(), name='loop_server', daemon=False).start()
    print("Please  'Ctrl+C' for exit. Type your message: ")