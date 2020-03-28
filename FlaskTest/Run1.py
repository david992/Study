from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "First Page!"

@app.route("/login")
def login():
    return "这是登录页面"
#反向解析login地址
@app.route("/url")
def url_login():
    login_url=url_for("login")
    print(login_url)
    resp = "<a href = '"+login_url+"'> 我要登录</a>"
    return resp

@app.route("/register")
def register():
    return "这是注册页面"

@app.route("/show/<name>")
def show1(name):
    return "<h>姓名：%s<h>" %name

@app.route("/<name>/<int:age>")
def show(name,age):
    # <int:age>:指定类型为int型
	return "<h>姓名为%s的年龄是%d<h>" %(name,age)

#反向解析show地址
@app.route("/urll")
def url_show():
    show_url = url_for("show",name="name",age=24)
    print((show_url))
    resp = "<a href = '" +show_url+ "'> "  +  show_url+ "</a>"
    return resp

#多URL路由
@app.route("/")
@app.route("/index")
@app.route("/<int:page>")
@app.route("/index/<int:page>")
def show2(page=None):
    if page is None:
        page = 1
    return "当前页面为:%d"%page

@app.route("/post",methods=["POST"])
def post():
    return "这是post请求方式访问的"
if __name__ == "__main__":
    app.run(debug=True)
