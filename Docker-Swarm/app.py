from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    prn = request.form['prn']
    branchname = request.form['branchname']
    return f'Welcome {username} to CDAC your PRN is {prn}, you are enrolled to course {branchname}'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
