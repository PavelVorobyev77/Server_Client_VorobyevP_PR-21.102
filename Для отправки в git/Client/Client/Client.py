
import socket
import threading

print("client start")

# ����������� � �������
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# ������� ��� ������ ��������� �� �������
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode().strip("b'")
            print(message)
        except:
            # ���� �������� ������, �� ������� �� �����
            print('An error occurred!')
            client_socket.close()
            break

# ������� ��� �������� ��������� �� ������
def send():

    print("enter your nickname as a first message")

    while True:
        message = input()
        client_socket.sendall(message.encode())


#������ ��� ��������� ��������� �� ������� � ��������

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()