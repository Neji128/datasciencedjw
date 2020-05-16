from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def Resume():
    return render_template('resume.html')

@app.route('/projects')
def Projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run()
