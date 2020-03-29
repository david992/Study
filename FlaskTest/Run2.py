from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    resp =  render_template("index.html")
    return resp
    print(resp)

@app.route("/index_extends")
def index_extends():
    return render_template("index_extends.html")

if __name__ == "__main__":
    app.run(debug=True)
