import socket

portas = [21, 23, 80, 443]
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex(('#', porta))
    if codigo == 0:
        print(porta, 'Open')
    cliente.close()