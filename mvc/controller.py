from flask import Flask
from flask import request
from flask import render_template

from mvc.model import Model

app = Flask(__name__)


@app.route('/')
def index():
    '''This is the default landing page'''

    print('instantiating a default model')
    model = Model()

    print('updating default view with default model')
    return render_template('view.html', data=model)


@app.route('/update/post', methods=['POST'])
def update_post():
    '''This is the route to update the number shown on the view'''

    print('updating the model with the new number from a POST request')
    model = Model(request.form['number'])

    print('updating the view with the new model')
    return render_template('view.html', data=model)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
