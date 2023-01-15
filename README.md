# Socket server and client - Python with Docker
Socket server  Сокет сервер - Программа на которой запущены серверные сокеты. Сокет клиент - Программа использующая клиентские сокеты. Вся эта схема, вместе взятая, образует клиент-серверную модель взаимодействия.  Суть ее в том, что разные клиенты подключаются к одному серверу, который координирует и управляет работой клиентов. Адрес сервера обычно публичный и его знают все клиенты. В основном подключение инициируется клиентом.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](#)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

### Create image docker:
```python
docker build --target Server_sock -t socket-server .
docker build --target Client_sock -t socket-client .
```

### Create network:
```python
docker network create my_socket_ipc_network
```
### Run scripts in different terminals:
```python
docker run -i -t --rm --network=my_socket_ipc_network --name socket-server_dns_name socket-server
```
```python
docker run -i -t --rm --network=my_socket_ipc_network socket-client
```
