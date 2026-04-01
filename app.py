from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
   return '<h1>Hello, World!</h1>'

@app.route('/about/<usuario>')
def about(usuario):
    return '<h3>About Page</h3><p>This is a simple Flask application. Hello, {}!</p>'.format(usuario)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
   