import socket


class Client:

    def __init__(self) -> None:
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)

    def conenct(self, address: str, port: int, timeout: float) -> None:
        self.close()

        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)

        self.socket.connect((address, port))
        self.socket.settimeout(timeout)

    def send(self, data: str, encoding: str = 'utf-8') -> int:
        return self.socket.send(bytes(data, encoding))

    def recv(self, recv_size: int = 1024, encoding: str = 'utf-8') -> str:
        return self.socket.recv(recv_size).decode(encoding)

    def close(self):
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass

        self.socket.close()
