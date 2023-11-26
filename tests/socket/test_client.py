import random
from common_library import socket


def test_conenct():

    def serverJob(client):
        client.send(bytes("greeting", 'utf-8'))
        data = client.recv(1024).decode('utf-8')
        client.send(bytes("[response] : " + data, 'utf-8'))
        client.close()

    port = random.randrange(15000, 20000)

    server = socket.Server()

    server.start(address='0.0.0.0',
                 port=port,
                 listen_size=10,
                 serverJob=serverJob)

    client = socket.Client()
    client.close()
    client.conenct(address='127.0.0.1', port=port, timeout=3)

    data = client.recv()
    assert data == "greeting"

    send_len = client.send("data")
    assert send_len == 4

    data = client.recv()
    assert data == "[response] : data"

    client.close()

    server.stop()


def test_send():
    test_conenct()


def test_recv():
    test_conenct()


def test_close():
    client = socket.Client()
    client.close()
