from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('/index.html')

@app.route('/fin')
def salir():
    return "<h1> Adios</h1>"

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
