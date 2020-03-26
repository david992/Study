from flask import Flask

#当前运行的主程序构建为flask的应用
#以便接受用户的请求（request）并给出响应（response）
app = Flask(__name__)

#flask中的路由定义，定义用户的访问路径
@app.route('/')

#匹配上路由定义的访问路径后的处理程序
#---视图函数--- 该函数必须要有return
#return 一个字符串或者响应对象
def index():
    return "This is my first flask app"

if __name__ == "__main__":
    #启动flask服务
    app.run(debug=True)