from flask import Flask, app,render_template,request 
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return "hello world\n"

@app.route('/hello/<username>')#dynamic route
def hello_user(username):
    return 'Welcome to the website %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0') #open for everyone
