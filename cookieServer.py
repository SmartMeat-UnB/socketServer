import socket

host = ''
port = 5560

#Definindo um valor de informacao de teste para ser transferido.
storedValue = "Hello Wolrd" 

#Definindo a configuracao de conexao
def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind(host, port)
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(1) #Permite uma conexao por vez.
    conn, addres = s.accept()
    print("Connected to: "+addres[0] + ":" + str(address[1]))
    retunr conn

def GET():
    reply = storesValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn)
    #Um loop que recebe e envia mensagens
    while True:
        #receber os dados
        data = conn.recv(1024)
        #Python 3 necessita da diferenciacao de dados entre bytes e strings
        #Significa que para receber temos que decodificar
        #Para enviar temos que codificar
        data = data.decode('utf-8') #utf-8 e string
        #Dividir os dados de forma que separe o comando do resto dos dadoss
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our cliente hates us :(")
            break
        elif command == "KILL":
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = "Unkown Command"

        #enviar dados ao cliente
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
      

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break

    
