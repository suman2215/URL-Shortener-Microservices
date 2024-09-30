from flask import Flask, request, jsonify
from pymongo import MongoClient
import string, random
import requests

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://mongodb:27017/")
db = client.urlshortener
url_collection = db.urls

def generate_short_id(num_of_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json['url']
    short_id = generate_short_id()
    url_collection.insert_one({'original_url': original_url, 'short_id': short_id})

    # Set the value in the caching service
    cache_data = {'key': short_id, 'value': original_url}
    cache_response = requests.post('http://caching-service:5003/set', json=cache_data)

    if cache_response.status_code != 200:
        return jsonify({"error": "Failed to cache the URL"}), 500

    return jsonify({"shortened_url": f"http://{request.host}/{short_id}"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
