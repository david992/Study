from flask import Flask, make_response, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
import pymysql
from werkzeug.utils import redirect
from json import dumps
pymysql.install_as_MySQLdb()
app = Flask(__name__,template_folder="temp_cookie",
            static_url_path="/static",
            static_folder="static")
# 指定连接字符串
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123456@localhost:3306/flask"
# 自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 自动追踪程序修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =  True
app.config["SECRET_KEY"] = "INPUT A STRING"
db = SQLAlchemy(app)


class Login(db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname = db.Column(db.String(50),nullable = False)
    pwd = db.Column(db.String(50),nullable= False)
    realname = db.Column(db.String(50),nullable=False)
    def __init__(self,uname,pwd,realname):
        self.pwd = pwd
        self.uname = uname
        self.realname = realname
    def __repr__(self):
        return "<Login %r>"%self.realname
#     将当前对象中所有属性封装到一个字典中
    def to_dict(self):
        dic={
            'id':self.id,
            'uname':self.uname,
            'pwd':self.pwd,
            'realname':self.realname
        }
        return dic
db.create_all()


@app.route("/set_session")
def set_session():
    session['uname'] = "david1"
    return "set ok "
@app.route("/get_session")
def get_session():
    username = session["uname"]
    return "session:"+username
@app.route("/del_session")
def del_session():
    del session["uname"]
    return "del ok"


@app.route("/get_cookie")
def get_cookie():
    username = request.cookies["username"]
    key = request.cookies.get("key")
    print(" %s %s"%(username,key))
    return "get cookie ok"
@app.route("/set_cookie")
def set_cookie():
#     将响应内容构建成响应对象
    resp = make_response("set cookie success")
    resp.set_cookie("key","123456",max_age=60*60)
    resp.set_cookie("username","david")
    return resp

@app.route("/login_cookie",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        # 判断之前是否成功登录过
        if "id" in request.cookies and "uname" in request.cookies:
            return "已登录"
        return  render_template("login.html")
    else:
        # 接收用户名和密码
        uname = request.form["uname"]
        pwd = request.form.get("pwd")
        # 验证密码用户名是否正确
        login = Login.query.filter_by(uname=uname,pwd=pwd).first()
        if login:
            resp = make_response("登录成功")
            # 正确的话，判断是否记住密码
            if "isSaved" in request.form:
                # id和name存进cookie
                resp.set_cookie("id", str(login.id), max_age=60*60)
                resp.set_cookie("uname", uname, max_age=60*60)
            return resp
        else:
            # 不正确
            return "用户名或密码错误"

@app.route("/sign_in",methods=["GET","POST"])
def sign_in():
    if request.method == "GET":
        if "id" in session and "uname" in session:
            id=session["id"]
            uname=session["uname"]
            return redirect("/index")
        elif "id" in request.cookies and "uname" in request.cookies:
            id = request.cookies["id"]
            uname = request.cookies.get("uname")
            return render_template("index.html",values = locals())
        return render_template("sign_in.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        login = Login.query.filter_by(uname=uname,pwd=pwd).first()
        if login:
            session["id"] = login.id
            session["uname"] = login.uname
            # return redirect ("/index")
            resp = make_response(render_template("index.html",values=locals()))
        # 正确的话，判断是否记住密码
            if "isSaved" in request.form:
            # id和name存进cookie
                resp.set_cookie("id", str(login.id))
                resp.set_cookie("uname", uname )
            return resp
        else:
            return render_template("sign_in.html")

@app.route("/index")
def index():
    if "id" in  session and "uname" in session:
        uname = session["uname"]
    return render_template("index.html",values = locals())

@app.route("/sign_out")
def sign_out():
    if "id" in session and "uname" in session:
        del session["id"]
        del session["uname"]
    return redirect("/index")

@app.route("/create_xhr")
def create_xhr():
    return render_template("xhr.html")

@app.route("/01getxhr")
def getxhr():
    return render_template("01getxhr.html")

@app.route("/02get")
def get():
    return render_template("02get.html")
@app.route("/02server")
def server02_views():
    return "ajax 请求"

@app.route("/03get")
def get03_views():
    return render_template("03get.html")
@app.route("/03server")
def server03_views():
    uname = request.args["uname"]
    return  "welcome %s"%uname

@app.route("/04post")
def post04_views():
    # uname = request.form["uname"]
    return  render_template("04post.html")
@app.route("/04server" ,methods=["POST"])
def server04_views():
    uname = request.form["uname"]
    age = request.form["age"]
    return  "welcome %s的%s"%(age,uname)

@app.route("/05checkname")
def checkname05_views():
    return  render_template("05checkname.html")
@app.route("/05server",methods=["POST"])
def server05_views():
    uname = request.form["username"]
    user = Login.query.filter_by(uname=uname).first()
    if user :
        return "已存在"
    else:
        return "ok"
@app.route("/json")
def json():
    return render_template("json.html")

@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/json02")
def json02():
    list=[
        {
            "name": "david",
            "age": 24,
            'gender': 'female'
        },
        {
            "name": "david999",
            "age": 24,
            'gender': 'male'
        }
    ]
    dic={
        "name":"david",
        "age":24,
        'gender':'female'
    }
    jsonstr = dumps(list)
    return jsonstr

@app.route("/json_login")
def json_login():
    login = Login.query.filter_by(id=1).first()
    list =[]
    for u in login:
        list.append(u.todict)
    return dumps(list)

@app.route("/01login")
def login01():
    return render_template("01login.html")
@app.route("/01server")
def server01():
    login = Login.query.all()
    list=[]
    for u in login:
        list.append(u.to_dict())
    return dumps(list)

if __name__ == "__main__":
    app.run(debug=True)