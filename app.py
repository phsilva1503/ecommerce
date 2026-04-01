from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('home.html')

'''
@app.route('/about/<usuario>')
def about(usuario):
    return '<h3>About Page</h3><p>This is a simple Flask application. Hello, {}!</p>'.format(usuario)
    '''



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
   