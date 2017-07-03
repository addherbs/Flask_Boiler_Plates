from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    testList = [{'title': '1'} , {'title': '2'}, {'title': '3'}]
    lists = ['Aditya' , 'Devendra', 'Pandey', 'Parul' , 'Amrit' , 'Mummy']
    return render_template('index.html', testList = testList, lists = lists)

if __name__ == '__main__':
    app.run()
