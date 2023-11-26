import socket
import threading


class Server:

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)

    def __job(self, address: str, port: int, listen_size: int, serverJob,
              timeout: float):
        self.socket.bind((address, port))
        self.socket.listen(listen_size)
        self.lock.acquire()
        while self.lock.locked():
            try:
                (client, clientAddress) = self.socket.accept()
                client.settimeout(timeout)

                t = threading.Thread(target=serverJob, args=(client, ))
                t.start()
            except Exception:
                if self.lock.locked() == False:
                    break

    def start(self, address: str, port: str, listen_size: int, serverJob):
        t = threading.Thread(target=self.__job,
                             args=(address, port, listen_size, serverJob, 10))
        t.start()

    def stop(self):
        if self.lock.locked():
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass

            self.socket.close()

            self.lock.release()
