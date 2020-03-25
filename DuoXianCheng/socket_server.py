from socketserver import *
#创建服务器类

class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        #self.request 等价accept 返回的套接字
        print("connect from ",self.request.getpeername())

        while True:
            data = self.request.recv(1024)
            if  not data :
                break
            print(data.decode())
            self.request.send(b"receive")

if __name__ == "__main__":

    server_addr = ("0.0.0.0",8888)

    #创建服务器对象
    server = Server(server_addr,Handler)

    #启动服务器
    server.serve_forever()