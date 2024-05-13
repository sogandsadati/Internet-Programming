import socket
import sys


def main():
    try:
        # create a TCP socket (SOCK_STREAM)
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    except socket.error as err:
        print("Error during creation of the socket")
        print(f"Reason: {err}")
        sys.exit()

    print("Socket created")

    target_host = "localhost"  # 127.0.0.1 is the same
    target_port = 32000
    addr = (target_host, target_port)
    s.bind(addr)
    s.listen(5)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Waiting for new connection")
    c_sock, c_addr = s.accept()
    print(f"Client connected from f{c_addr}")
    d = c_sock.recv(100000)
    print(f"Data received {d}")
    c_sock.send("Hello from server".encode())
    c_sock.close()
    s.close()


main()
