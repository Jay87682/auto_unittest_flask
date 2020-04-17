from flask import Flask

app = Flask(__name__)

@app.route('/int_test/<int:value>')
def demo_int(value):
    print(type(value))
    return str(value)
@app.route('/str_test/<string:string>')
def demo_string(string):
    print(type(string))
    return string

@app.route('/float_test/<float:fvalue>')
def demo_float(fvalue):
    print(type(fvalue))
    return str(fvalue)

@app.route('/path_test/<path:path>')
def demo_path(path):
    print(type(path))
    return path


if __name__ == '__main__':
    #app.run(port=6666, host='0.0.0.0', debug=True)
    app.run(port=8888, host='0.0.0.0')
