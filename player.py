class Player:
    def __init__(self, name, conn):
        self.name = name
        self.conn = conn
        self.count_items = 0

    def send_message(self, message):
        self.conn.send(message.encode())

    def receive(self):
        return (self.conn.recv(1024)).decode()