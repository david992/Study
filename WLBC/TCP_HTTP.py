from  socket import  *

#创建tcp套接字
s = socket()
s.bind(("127.0.0.1",8000))
s.listen(5)

while True:
    c,addr=s.accept()
    print("Cinnect from ",addr)

    data = c.recv(4096)
    print("****************")
    print(data)
    print("****************")

    data='''http/1.1 200 ok \n
    Content-Encoding: gzip
    Content-Type: text/html
    
    <h1>welcome to david!</h1>
    <p>这是测试</p>'''

    c.send(data.encode())
    c.close()
s.close()