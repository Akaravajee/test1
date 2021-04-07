from flask import Flask
server = Flask(__name__)

@server.route("/")
def Home():
    return "<h1>อัคราวจี แจ้งศรี 6006021630032</h1>";


if __name__ == "__main__":
    #app.run(debug=True)
    server.run(host='0.0.0.0', port=80)
