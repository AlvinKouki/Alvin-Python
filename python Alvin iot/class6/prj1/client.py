import socket

s = socket.socket()
s.connect(('127.0.0.1', 5487))  #連到伺服器

while 1:
    msg = input('Input Message:')  # 輸入想要傳送到伺服器的訊息
    s.send(msg.encode('utf8'))  #將訊息編碼傳送出去
    reply = s.recv(128).decode('utf8')  #接受伺服器回傳的訊息並解碼
    if reply == 'quit':
        print('Disconnected')
        s.close()
        break
    print(reply)