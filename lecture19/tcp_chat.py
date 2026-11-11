import socket
from threading import Thread

HOST = ('127.0.0.1', 8888)
SOCK_PROTOCOL = (socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP
ANSI = {
    'red': '\033[91m',
    'blue': '\033[94m',
    'reset': '\033[0m',
    'clearline': '\033[A\033[K'  # move cursor up one line and delete
}

disconnected = False

def on_disconnect():
    global disconnected
    if not disconnected:
        disconnected = True
        print("Partner has disconnected. Press enter to exit.")
    exit()

def send_msg(c):
    while True:
        try:
            msg = input()
            print(ANSI['clearline'], end='')
            c.send(msg.encode('utf-8'))
            print(f"{ANSI['red']}You: {ANSI['reset']}" + msg)
        except:
            on_disconnect()

def recv_msg(c):
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                c.close()
                on_disconnect()
            print(f"{ANSI['blue']}Partner: {ANSI['reset']}" + msg.decode('utf-8'))
        except:
            on_disconnect()

if __name__ == "__main__":
    choice = input("Do you want to be server or client? (s/c): ").lower()
    if choice == 's':  # server
        server = socket.socket(*SOCK_PROTOCOL)  # * unpacks the tuple into both args
        server.bind(HOST)
        server.listen()
        print("Waiting for connection...")
        client, addr = server.accept()
        print("Connected to", addr)
        print("Use 'Ctrl+C' to disconnect.")
    elif choice == 'c':  # client
        print("Connecting to server...", end='')
        client = socket.socket(*SOCK_PROTOCOL)
        client.connect(HOST)
        print("success! Connected to", client.getpeername())
        print("Use 'Ctrl+C' to disconnect.")
    else: exit()

    try:
        send_thread = Thread(target=send_msg, args=(client,), daemon=True)
        recv_thread = Thread(target=recv_msg, args=(client,), daemon=True)
        send_thread.start()
        recv_thread.start()
        send_thread.join()
        recv_thread.join()
        # Daemon threads exit when the main thread exits
    except KeyboardInterrupt:
        disconnected = True
        print("\nDisconnecting... Press enter to exit.")
        client.close()
    