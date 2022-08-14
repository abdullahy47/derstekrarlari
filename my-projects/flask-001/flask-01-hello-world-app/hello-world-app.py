from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask"

@app.route('/second')
def second():
    return "Bu ikinci sayfadır"

@app.route('/third/subthird')
def third():
    return "Bu da üçüncü sayfa"

@app.route('/forth/<string:id>')
def forth(id):
    return f"Bu da dördüncü sayfanın id'si {id}"

if __name__ == '__main__':
    app.run(debug=True)