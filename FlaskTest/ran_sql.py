from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql
from sqlalchemy import or_, desc, asc
from werkzeug.utils import redirect

pymysql.install_as_MySQLdb()

app = Flask(__name__)
#指定连接字符串
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#指定让sqlalchemy自动追踪程序的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
# 执行完操作后自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
#为当前项目创建sqlalchemy实例
db = SQLAlchemy(app)


#创建实体类-Models
#创建users 映射到表中叫users表
# id:主键,自增
# username: 长度80 字符串 不允许为空 必须唯一
# age: 整数 允许为空值
# email: 长度120的字符串  唯一

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email
    def __repr__(self):
        return "<Users:%r>"%self.username

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)
    def __init__(self,sname,sage):
        self.sage = sage
        self.sname = sname
    def __repr__(self):
        return "<Student:%r>"%self.sname

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)
    def __init__(self,tname,tage):
        self.tage = tage
        self.tname = tname
    def __repr__(self):
        return "<Teacher:%r>"%self.tname

class Course(db.Model):
    __tableable__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30))
    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Teacher:%r>"%self.cname
#暴力删除表
# db.drop_all()
#创建好的实体类映射到数据库
db.create_all()
@app.route("/")
def index():
    return render_template("user_index.html")
@app.route("/insert")
def insert_views():
#     创建users对象
    users = Users("david",24,"24604567@qq.com")
#     将对象通过db.session.add()加入到数据库
    db.session.add(users)
#     提交插入操作
#     db.session.commit()
    return "insert Success"

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("sql_register.html")
    else:
        # 接收前端传输的数据
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
        #数据构成users对象
        users = Users(username,age,email)
        #将对象通过db.session.add()加入到数据库
        db.session.add(users)
        #提交插入操作
        # db.session.commit()
        return redirect("query_all")

@app.route("/query")
def query_views():
    users = db.session.query(Users).order_by(Users.id.desc()).all()
    for u in users:
        print(u.age,u.username,u.email)
    return "Query OK"

@app.route("/filter")
def filter_views():
    users = db.session.query(Users).filter(Users.age>20,Users.username=="david").all()
    for u in users:
        print(u.age,u.email,u.username)
    print("***********")
    users1= db.session.query(Users).filter(or_(Users.age>20,Users.username=="1805059003")).all()
    for u in users1:
        print(u.age, u.email, u.username)
    print("***********")
    users2 = db.session.query(Users).filter(Users.username.like('%av%')).all()
    for u in  users2:
        print(u.age,u.username,u.email)
    print("***********")
    users3 = db.session.query(Users).filter(Users.id.in_([1,2,3])).all()
    for u in  users3:
        print(u.id,u.age,u.username,u.email)
    return "Query OK"

@app.route("/query_all")
def query_all():
    #根据id降序排列，以age升序做第二准则
    users = db.session.query(Users).order_by(desc(Users.id),asc(Users.age)).all()
    #按照age分组显示
    # users = db.session.query(Users.age).group_by("age").all()
    print(users)

    return  render_template("users.html",values = locals())

# 方法1
# @app.route("/query_id/<int:id>")
# def query_id(id):
#     users = db.session.query(Users).filter_by(id=id).first()
#     return render_template("usersid.html",values=locals())

# 方法2
@app.route("/query_id")
def query_id():
    # 接收前台传来的id
    id = request.args.get("id")
    users = db.session.query(Users).filter_by(id=id).first()
    return render_template("usersid.html",values=locals())

@app.route("/delete")
def delete():
    # 接收前台传来的id
    id = request.args.get("id")
    users = Users.query.filter_by(id= id).first()
    db.session.delete(users)
    url = request.headers.get("referer","/query_all")
    return redirect(url)

@app.route("/update",methods=["GET","POST"])
def update():
    if request.method == "GET":
        id = request.args.get("id")
        user = db.session.query(Users).filter_by(id=id).first()
        return render_template("update.html",values=locals())
    else:
    #     接收前端传递的参数
        id = request.form["id"]
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
    #查询
        user = db.session.query(Users).filter_by(id=id).first()
    #修改
        user.username = username
        user.age = age
        user.email =email
    #保存
        db.session.add(user)
        return  redirect("/query_all")
    # user = Users.query.filter_by(id=3).first()  # 查询
    # user.username = "david"     # 修改
    # user.age = 24
    # user.email = "24604567@qq.com"
    # db.session.add(user)   #保存
if __name__ == "__main__":
    app.run(debug=True)