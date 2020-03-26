from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    resp =  render_template("index.html")
    return resp
    print(resp)

if __name__ == "__main__":
    app.run(debug=True)
