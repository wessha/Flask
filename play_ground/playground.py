from flask import Flask, render_template

ground = Flask(__name__)

@ground.route('/play')
@ground.route('/play/<int:x>')
@ground.route('/play/<int:x>/<color>')
def play(x, color):
    return render_template('play.html', x=x, color=color)

if __name__ == '__main__':
    ground.run(debug=True)
