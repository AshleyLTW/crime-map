# import camelot
# tables = camelot.read_pdf('https://www.hupd.harvard.edu/files/hupd/files/040219.pdf')
# tables.export('foo.csv', f='csv')

# print("hello world")

from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

