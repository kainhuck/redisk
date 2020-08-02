# connect

from socket import socket, AF_INET, SOCK_STREAM

def connect(host="127.0.0.1", port=6379):
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    tcpSocket.connect((host, port))

    return tcpSocket