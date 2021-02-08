import socket, threading

#------------serveur local basique------------
HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

server.listen()

clients = []
usernames = []

#--------------envoi de message---------------

def envoi(message):
    for client in clients:
        client.send(message)

#--------------nouvelles connexions---------------

def nvconnexions():
    while True:
        client, adresse = server.accept()
        print(f"Connected with {str(adresse)} !")

        client.send("MAX".encode('utf-8'))
        username = client.recv(1024)

        username.append(usernames)
        client.append(client)
        print(f"Username of the client is {username}")
        envoi(f"{username} est connecté au serveur!\n".encode('utf-8'))
        client.send("Connecté au serveur".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start

#--------------handler----------------------

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{usernames[clients.index(clients)]} says {message}")
            envoi(message)
        except:
            index = client.index(clients)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            break

print("Serveur en marche---")