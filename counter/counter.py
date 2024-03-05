from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0

    session['counter'] += 1

    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment_by_two')
def increment_by_two():
    if 'counter' not in session:
        session['counter'] = 0

    session['counter'] += 2

    return render_template('index.html', counter=session['counter'])

if __name__ == '__main__':
    app.run(debug=True)
