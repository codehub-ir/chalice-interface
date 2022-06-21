from chalice import Chalice
from requests import get, post
from os import path

app = Chalice(app_name='mychalice')

api = 'http://codehub.pythonanywhere.com/api/v1/'

@app.route('/event')
def list_event():
    uri = 'event'
    context = get(
        path.join(api, uri)
    ).json()
    return context

@app.route('/snippet', methods=['POST'])
def create_snippet():
    uri = 'snippet'
    snippet = app.current_request.json_body
    response = post(
        path.join(api, uri),
        data=snippet
    ).json()
    return response
