from flask import Flask
app = Flask(__name__)
@app.route('/')
def Hi():
    return "Hi,I am Chessie Mkashai what about you?"
if __name__ == '__main__':
    app.run(debug=True)
    