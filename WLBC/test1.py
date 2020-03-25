import  socket
name=socket.gethostname()
ip = socket.gethostbyname("localhost")
print(socket.gethostbyaddr("www.baidu.com"))
print(socket.inet_aton("127.0.0.1"))
print(socket.getservbyname("ssh"))
print(socket.getservbyport(80))
print(ip)
print(name)