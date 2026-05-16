
from flask import Flask, jsonify
app = Flask(__name__)

# Home page - shows when you visit the website
@app.route('/')
def home():
    return '''
    <h1>CMPS465 CI/CD Project — Updated!</h1>
    <p>Student: kwg255 - Beirut Arab University</p>
    <p>Version 2.0 - Deployed automatically via GitHub Actions</p>
    '''

# Health check - Azure uses this to verify app is running
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "student": "kwg255"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
