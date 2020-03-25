#coding=utf-8
'''
http server v2.0
'''
from socket import  *
from threading import Thread
import  sys,traceback

class httpserver(object):
    """
    封装具体的服务器功能
    """
    def __init__(self,server_addr,static_dir):
        #增添服务器对象属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.socket = socket()
        self.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.socket.bind(self.server_address)

    def server_forever(self):
        self.socket.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            try:
                c,addr = self.socket.accept()
            except KeyboardInterrupt:
                self.socket.close()
                sys.exit("服务器退出")
            except Exception:
                traceback.print_exc()
                continue
            #创建新的线程处理请求
            clientThread = Thread(target=self.handleRequest,args=(c,))
            clientThread.setDaemon(True)
            clientThread.start()
    def get_html(self,c,getRequest):
        if getRequest == "/":
            filename = self.static_dir + "/index.html"
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename,encoding='utf-8')
        except Exception:
            responseHeaders ="HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders +="\r\n "
            responseBody = "Sorry,the page is not found"
        else:
            responseHeaders = "HTTP/1.1 200  OK\r\n"
            responseHeaders += "\r\n "
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            c.send (response.encode())

    #客户端请求函数
    def handleRequest(self,c):
        #接收客户端请求
        request = c.recv(4096)
        # print(request)
        #解析请求内容
        requestHeaders = request.splitlines()
        print(c.getpeername(),":",requestHeaders[0])
        #获取具体请求内容
        getRequest = str(requestHeaders[0]).split(" ")[1]
        if getRequest == "/" or getRequest[-5:] ==  ".html":
            self.get_html(c,getRequest)
        else:
            self.get_data(c,getRequest)
        c.close()
    def get_data(self,c,getRequest):
        urls = ["/time","/python"]
        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            if getRequest == "/time":
                import  time
                responseBody = time.ctime()
            elif getRequest =="/python":
                responseBody ="python ~~~~~~~~~~~"
        else:
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += "\r\n "
            responseBody = "Sorry,the data is not found"
        response = responseHeaders + responseBody
        c.send(response.encode())


if __name__ == "__main__":
    server_addr = ("0.0.0.0",8888)
    static_dir = "../html"

    #生成对象
    httpd = httpserver(server_addr,static_dir)
    #启动服务器
    httpd.server_forever()