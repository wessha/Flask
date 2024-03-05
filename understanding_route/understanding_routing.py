from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:count>/<word>')
def repeat_word(count, word):
    return word * count

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again.", 404

if __name__ == '__main__':
    app.run(debug=True)

