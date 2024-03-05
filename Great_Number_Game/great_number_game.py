from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def generate_random_number():
    return random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'random_number' not in session:
        session['random_number'] = generate_random_number()
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        if guess == session['random_number']:
            return redirect(url_for('winner'))
        elif guess < session['random_number']:
            return render_template('index.html', message='Too low!', attempts=session['attempts'])
        else:
            return render_template('index.html', message='Too high!', attempts=session['attempts'])

    return render_template('index.html')

@app.route('/winner')
def winner():
    random_number = session.pop('random_number')
    attempts = session.pop('attempts')
    return render_template('winner.html', random_number=random_number, attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True)
