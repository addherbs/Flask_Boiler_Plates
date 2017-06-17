from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def index():
    return 'this is the lol homepage'

@app.route('/profile')
def profile():
    return 'lol this is the profile page dude'

@app.route('/profile/<username>', methods=['GET','POST'])
def username(username):
    return render_template('profile.html', username = username)


if __name__ == '__main__':
    app.run()
