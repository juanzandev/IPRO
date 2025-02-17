from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app) # Enalbe CORS for all routs

@app.route('/email', methods=['POST'])
def receive_email():

    # Log request methods and headers
    print(f"\nRequest Method: {request.method}")
    print(f"Request Headers: {request.headers}")

    data = request.json
    subject = data.get('subject', 'No Subject')
    body = data.get('body', 'No Body')
    
    print(f"\nEmail Received:\nSubject: {subject}\nBody: {body[:500]}...")  # Print first 500 characters
    
    # Add your processing logic here
    # Example: Save to file or database
    
    return jsonify({"status": "success", "message": "Email processed successfully!"})

if __name__ == '__main__':
    app.run(port=5000)