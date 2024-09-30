from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL Shortening Route
@app.route('/shorten', methods=['POST'])
def shorten_url():
    response = requests.post('http://url-shortener-service:5001/shorten', json=request.json)
    return jsonify(response.json()), response.status_code

# URL Redirection Route
@app.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    cache_response = requests.get(f'http://caching-service:5003/get/{short_id}')
    if cache_response.status_code == 200:
        return cache_response.content, cache_response.status_code
    response = requests.get(f'http://url-redirection-service:5002/{short_id}')
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
