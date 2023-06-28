from flask import Flask, render_template

app = Flask(__name__)


dataList = [{'id': 1, 'name': 'Sadhat'}, {'id': 2, 'name': 'Hameed'}]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=dataList)


if __name__ == '__main__':
    app.run()
