# coding: utf-8
from flask import Flask, request, render_template


from LocationPlan import input_tip

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('hello.html')

@app.route('/inputloc', methods=['GET'])
def signin_form():
    return render_template('demo.html')

@app.route('/inputloc', methods=['POST'])
def signin():
    worklocation = request.form['worklocation']
    complete_addr = input_tip(worklocation)
    # return render_template('signok.html', username=worklocation)
    return render_template('demo.html', showcomplete=complete_addr)

if __name__ == '__main__':
    app.run(port=8888)