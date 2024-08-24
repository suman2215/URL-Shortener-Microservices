from flask import Flask, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://mongodb:27017/")
db = client.urlshortener
url_collection = db.urls

@app.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    url_data = url_collection.find_one({'short_id': short_id})
    if url_data:
        return redirect(url_data['original_url'])
    return {"message": "URL not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
