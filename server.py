from flask import Flask
import compiler

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def index():
    try:
        code = compiler.compile(request.form['program'])
        return code
    except compiler.BrainfuckCompilerError:
        return '', 400

if __name__ == '__main__':
    print('Serving on :3000')
    app.run(port=3000)
