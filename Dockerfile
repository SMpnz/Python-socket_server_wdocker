#first stage
FROM python:3.11-slim AS Server_sock

# http://bugs.python.org/issue19846
# > В настоящий момент настройка "LANG=C" в Linux *полностью выводит из строя Python 3*, а это плохо.
ENV LANG C.UTF-8

WORKDIR /src
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py /src
EXPOSE 5051
EXPOSE 5051/udp
EXPOSE 9990:9999/udp

ENTRYPOINT [ "python" ]
CMD ["./server.py"]


#second stage
FROM python:3.11-slim AS Client_sock
ENV LANG C.UTF-8

WORKDIR /src
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY client.py /src
EXPOSE 5051
EXPOSE 5051/udp
EXPOSE 9990:9999/udp
ENTRYPOINT [ "python" ]
CMD ["./client.py"]
