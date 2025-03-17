from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/up')
def health():
    return '', 200

if __name__ == '__main__':
    # change the port to run on port 5001
    app.run(
        host='0.0.0.0',
        debug=False,
        port=5002)