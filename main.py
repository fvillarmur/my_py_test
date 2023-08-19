"""
Example of Flask RESTFul integration.
requires: `pip install flask-restful`
"""
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Flasgger RESTful',
    'uiversion': 2
}

@app.route('/hello')
def hello():
    """
        get endpoint
        ---
        tags:
            - hello
        responses:
            200:
                description: success    
    """
    return "hi"

swag = Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
