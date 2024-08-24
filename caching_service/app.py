from flask import Flask, request
import memcache

app = Flask(__name__)

# Memcached setup
cache = memcache.Client(['memcached:11211'], debug=0)

@app.route('/get/<key>', methods=['GET'])
def get_cache(key):
    value = cache.get(key)
    if value:
        return value, 200
    return {"message": "Key not found"}, 404

@app.route('/set', methods=['POST'])
def set_cache():
    key = request.json['key']
    value = request.json['value']
    cache.set(key, value, time=300)
    return {"message": "Cached successfully"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
