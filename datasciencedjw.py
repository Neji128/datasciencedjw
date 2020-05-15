from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Yo Yo Hello'

@app.route('/Projects')
def projects():
    return 'Recent Works'

if __name__ == "__main__":
    app.run()
