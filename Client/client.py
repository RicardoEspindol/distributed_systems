import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777 ))

    except:
        return print('\n Falha na conexão! \n')
    
    userName = input('Nome do cliente: ')
    print('\n  -> CONECTADO!!')

    thread1 = threading.Thread(target=receberMensagem, args=[client])
    thread2 = threading.Thread(target=enviarMensagem, args=[client, userName])

    thread1.start()
    thread2.start()

def receberMensagem(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\n Não foi possível permanecer conectado ao servidor! \n')
            print('Pressione <Enter> para continuar... \n')
            client.close()
            break

def enviarMensagem(client, userName):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{userName}> {msg}'.encode('utf-8'))
        except:
            return
main()