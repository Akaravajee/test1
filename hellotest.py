from flask import Flask
server = Flask(_name_)

@server.route("/")
def Home():
    return "<h1>อัคราวจี แจ้งศรี 6006021630032</h1>";


if _name_ == '_main_':
    #app.run(debug=True)
    server.run(host='0.0.0.0', port=80)
