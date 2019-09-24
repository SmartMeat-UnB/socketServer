import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ip do server
host = '192.168.0.9'
port = 5560

s.connect((host, port))

while True:
    command = input("Enter command: ")
    if command == 'EXIT':
        # Eviar sair pro server
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        #Envia para fechar o server
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()
