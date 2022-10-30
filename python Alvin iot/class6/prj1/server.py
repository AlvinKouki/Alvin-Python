import socket

HOST = "localhost"  #IP
PORT = 5487
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)  #伺服器端最多可接受多少socket
print('server:{} port:{} start '.format(HOST, PORT))
client, addr = s.accept()  #伺服器端接受並會回傳對象與IP位置資訊
print('client address:{}, port:{}'.format(addr[0], addr[1]))

while 1:
    msg = client.recv(100).decode("utf8")  #接收客戶端訊息
    print('Receive Message:' + msg)
    if msg == 'Hi':
        client.send(b'Hello')
    elif msg == "Bye":
        client.send(b'quit')
        break
    else:
        client.send(b'wtf')

client.close()
s.close