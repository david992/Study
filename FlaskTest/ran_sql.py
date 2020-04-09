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
    courses = db.relationship(
        "Course",
        secondary="student_course",
        lazy="dynamic",
        backref = db.backref(
            "students",
            lazy="dynamic"
        )
    )

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)
    # 增加一列course_id外键列
    course_id = db.Column(db.Integer,db.ForeignKey("course.id"))
    # 增加反向引用  与wife实体类中多一对一引用
    wife = db.relationship("Wife",uselist=False,backref="teacher")
    def __init__(self,tname,tage):
        self.tage = tage
        self.tname = tname
    def __repr__(self):
        return "<Teacher:%r>"%self.tname

class Wife(db.Model):
    __tablename__="wife"
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
    #增加一个列表式引用teacher的主键
    teacher_id = db.Column(db.Integer,db.ForeignKey("teacher.id"))
    def __init__(self,wname,wage):
        self.wage=wage
        self.wname=wname
    def __repr__(self):
        return "<Wife %r>"%self.wname

class Course(db.Model):
    __tableable__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30))
    # 反向引用，返回与当前课程相关的teacher表
    # backref：定义反向关系，在teacher实体中增加course属性，
    # 可替代course_id访问Course模型
    teachers = db.relationship("Teacher", backref="course", lazy="dynamic")
    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Teacher:%r>"%self.cname


student_course = db.Table(
    "student_course",
    db.Column("id",db.Integer,primary_key=True),
    db.Column("student_id",db.Integer,db.ForeignKey("student.id")),
    db.Column("course_id",db.Integer,db.ForeignKey("course.id"))
)

#暴力删除表
#db.drop_all()
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

@app.route("/register_user",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("user_register.html")
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
        return redirect("query_users")

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
    return "filter OK"

@app.route("/query_users")
def query_users():
    #根据id降序排列，以age升序做第二准则
    users = db.session.query(Users).order_by(desc(Users.id),asc(Users.age)).all()
    #按照age分组显示
    # users = db.session.query(Users.age).group_by("age").all()
    return  render_template("users.html",values = locals())

# 方法1
# @app.route("/query_id/<int:id>")
# def query_id(id):
#     users = db.session.query(Users).filter_by(id=id).first()
#     return render_template("users_query.html",values=locals())

# 方法2
@app.route("/query_id")
def query_id():
    # 接收前台传来的id
    id = request.args.get("id")
    users = db.session.query(Users).filter_by(id=id).first()
    return render_template("users_query.html",values=locals())

@app.route("/wife_query")
def query_wife():
    # teacher = Teacher.query.filter_by(tname="sss").first()
    # wife = teacher.wife
    # print("%s的夫人是：%s"%(teacher.tname,wife.wname))
    # return "ok"
    wife = Wife.query.order_by(desc(Wife.id)).all()
    return render_template("wife.html",values=locals())

@app.route("/query_tea/<int:id>")
def query_tea(id):
    teacher = Teacher.query.filter_by(id=id).first()
    return render_template("teachers_query.html",values=locals())

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

@app.route("/add_course")
def add_course():
    course1 = Course("python")
    course2 = Course("English")
    course3 = Course("mysql")
    course4 = Course("math")
    list = [course1,course2,course3,course4]
    for u in list:
        db.session.add(u)
    return "ok"
@app.route("/add_teacher")
def add_teacher():
    teacher = Teacher("蒋老师",24)
    # 根据course——id查询出一个course实体，再将实体赋给teacher
    course = Course.query.filter_by(id=1).first()
    teacher.course = course
    print(course)
    db.session.add(teacher)
    return "ok"

@app.route("/register_teacher",methods=["POST","GET"])
def register_teacher():
    if request.method == "GET":
        courses =   Course.query.all()
        return render_template("register_teacher.html",values=locals())
    else:
#         获取提交的数据
        tname = request.form["tname"]
        tage = request.form["tage"]
        course_id = request.form["course_id"]
#         根据提交的过来的course_id查询出对应的course对象
        course = Course.query.filter_by(id=course_id).first()
#         创建teacher对象并将course值赋给对象
        teacher = Teacher(tname,tage)
        teacher.course = course
#         保存
        db.session.add(teacher)
        return redirect("/query_teachers")

@app.route("/query_teachers")
def query_teacher():
    #course对象查询对应teacher对象
    # course = Course.query.filter_by(id = 1).first()
    # teachers = course.teachers.all()
    # print(teachers)
    #通过teacher查询course
    teacher = Teacher.query.order_by(desc(Teacher.tage)).all()
    # teacher= db.session.query(Teacher,Course).filter_by(Teacher.course_id ==Course.id).all()
    # teacher.course
    return render_template("teachers.html",values=locals())

@app.route("/wife_add")
def wife_add():
    # 查询某老师信息
    teacher = Teacher.query.filter_by(tname="sss").first()
    # 创建wife对象
    wife = Wife("SSS",18)
    wife.teacher = teacher
    # 将wife保存
    db.session.add(wife)
    return "ok"
@app.route("/wife_register",methods=["POST","GET"])
def wife_register():
    if request.method == "GET":
        #查询teacher列表 发送到模板上
        teacher = Teacher.query.all()
        return render_template("wife_register.html",values=locals())
    else:
        teacher_id = request.form.get("teacher_id")
        wife = Wife.query.filter_by(teacher_id=teacher_id).first()
        if wife is not None:
            errmsg = "已经存在配偶"
            teachers = Teacher.query.all()
            return  render_template("wife_register.html",values=locals())
        else:
            wname = request.form.get("wname")
            wage = request.form.get("wage")
            teacher = Teacher.query.filter_by(id=teacher_id).first()
            wife=Wife(wname,wage)
            wife.teacher=teacher
            db.session.add(wife)
            return redirect("/wife_query")

# 向多对多表中添加数据
@app.route("/add_atudent_course")
def add_student_course():
    stu = Student.query.filter_by(sname="aaaa").first()
    cour = Course.query.filter_by(id=1).first()
#     将course课程添加到student的courses列表中
    stu.courses.append(cour)
    db.session.add(stu)
    return "add ok ~~~"

@app.route("/query_student_course")
def query_student_course():
    student = Student.query.filter_by(id=1).first()
    student.courses.all()
    return "query ok ~~~"
if __name__ == "__main__":
    app.run(debug=True)