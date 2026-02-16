from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Python Learning Backend!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    print("🚀 Starting on http://localhost:8000")
    app.run(debug=True, host='localhost', port=8000)
