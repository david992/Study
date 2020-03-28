from flask import Flask,render_template

app = Flask(__name__)
class Person(object):
    def say(self):
        return " i am a person"

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
if __name__ == "__main__":
    app.run(debug=True)
