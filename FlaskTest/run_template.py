from flask import Flask, render_template, request, make_response
from gevent import os
from werkzeug.utils import redirect

app = Flask(__name__,template_folder="templates",
            static_url_path="/static",
            static_folder="static")
class Person(object):
    def say(self):
        return " i am a person"

@app.route("/")
def index():
    return  render_template("index.html")
@app.route("/login")
def login():
    return "这里是登录页面"

@app.route("/temp")
def temp():
    # dic = { "title":"我的第一个模板",
    #         "bookname":"钢铁是怎么炼成的",
    #         "author":"奥斯特洛夫斯基",
    #         "price":32.5,
    #         "publisher":"北京大学出版社"}
    # resp =  render_template("first_temp.html",values=dic)
    title="我的第一个模板"
    bookname="钢铁是怎么炼成的"
    author="奥斯特洛夫斯基"
    price=32.5
    publisher="北京大学出版社"
    list = ["1111","2222","3333","4444"]
    tup = ("刘德华","张学友","郭富城","黎明")
    dic = {
            "1":"one",
            "2":"two",
            "3":"three",
            "四":"four"}
    per = Person()
    per.name = "旗木卡卡西"
    uname = "   hello world     "
    resp =  render_template("first_temp.html",values=locals())
    return resp


@app.route("/inc")
def inc():
    return render_template("include_test.html",uname="测试变量")

@app.errorhandler(404)
def page_not_fonud(e):
    return render_template("404.html"),404

@app.route("/request")
def request_views():
    re = dir(request)
    #获取请求方案
    scheme = request.scheme
    #获取请求方式
    method = request.method
    # 获取get请求方式提交的数据
    args = request.args
    # 获取post请求方式提交的数据
    form = request.form
    # 获取任意请求方式提交的数据
    vaules = request.values
    #获取cookies中信息
    cookies  = request.cookies
    #获取消息头的信息
    headers = request.headers
    #获取请求的url的地址
    path = request.path
    #获取用户上传的文件
    files = request.files
    #获取请求源路径
    referer = request.headers.get("referer","")
    #获取请求的完整路径
    full_path = request.full_path
    #获取访问地址url
    url = request.url
    return render_template("request.html",values=locals())

@app.route("/get_args")
def form_view():
    return render_template("get_args.html")

@app.route("/form_do")
def form_do_view():
    if request.method == "GET":
        uname =  request.args.get("uname")
        pwd = request.args.get("upwd")
        print("name:%s,pwd:%s"%(uname,pwd))
    return "GET_OK"

@app.route("/post_form",methods=["GET","POST"])
def post_views():
    if request.method == "GET":
        return render_template("post_form.html")
    else:
        uname = request.form.get("uname")
        pwd = request.form.get("upwd")
        uemail = request.form.get("uemail")
        print("name:%s,pwd:%s,email:%s" % (uname, pwd, uemail))
    # return "POST_OK"
    #重定向到"/"地址
    return redirect("/")

# @app.route("/post_do",methods=["POST"])
# def post_do_view():
#     if request.method == "POST":
#         uname =  request.form.get("uname")
#         pwd = request.form.get("upwd")
#         uemail = request.form.get("uemail")
#         print("name:%s,pwd:%s,email:%s"%(uname,pwd,uemail))
#     return "POST_OK"

@app.route("/response")
def reponse_view():
    #构建响应对象
    resp = make_response(render_template("post_form.html"))
    return resp
    
@app.route("/file",methods=["GET","POST"])
def file_views():
    if request.method == "GET":
        return render_template("file.html")
    else:
        #接收客户端上传的name属性为uimg文件
        f = request.files["uimg"]
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        print(basepath)
        #获取上传图片名称
        filename = f.filename
        print("name:"+filename)
        #路径拼接到static目录下
        upload_path = os.path.join(basepath, "static/images/", filename)
        #文件保存
        f.save(upload_path)
        return "upload ok !"


if __name__ == "__main__":
    app.run(debug=True)
