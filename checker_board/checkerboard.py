from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html', rows=8, columns=8)

@app.route('/<int:x>')
def custom_checkerboard(x):
    return render_template('checkerboard.html', rows=8, columns=x)

@app.route('/<int:x>/<int:y>')
def custom_checkerboard_xy(x, y):
    return render_template('checkerboard.html', rows=x, columns=y)

if __name__ == '__main__':
    app.run(debug=True)
