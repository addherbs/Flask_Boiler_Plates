from flask import Flask, request

app =  Flask(__name__)

@app.route('/')
def index():
    return 'this is the lol homepage'

@app.route('/profile')
def profile():
    return 'lol this is the profile page dude'

@app.route('/profile/<int:username>', methods=['GET','POST'])
def username(username):
    if request.method == 'POST':
        return 'this is a post form'
    elif request.method == 'GET':
        return 'this is a GET form'


if __name__ == '__main__':
    app.run()
