from flask import Flask, render_template, request, jsonify
from ll import generate_response, extract_text_from_pdf
from flask_cors import CORS
import os
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB server
db = client['Chat_bot']  # Use 'chat_bot' database
history_collection = db['History']  # Use 'History' collection

# Extract PDF content once at startup
pdf_path = "./FirstAid_data.pdf"
if os.path.exists(pdf_path):
    pdf_content = extract_text_from_pdf(pdf_path)
else:
    print(f"Error: PDF file not found at {pdf_path}")
    pdf_content = ""

# Store conversation history in-memory (replace with DB for persistence)
conversation_history = []

def clean_format(response):
    cleaned_response = response.replace("Step 1:", "").replace("Step 2:", "").replace("Step 3:", "")
    cleaned_response = cleaned_response.replace("Step 4:", "").replace("Step 5:", "").replace("Step 6:", "").replace("Step 7:", "")
    return cleaned_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        response = generate_response(user_message, pdf_content)
        formatted_response = clean_format(response).replace("\n", "<br>")
        
        # Save conversation history
        conversation_entry = {"user": user_message, "ai": formatted_response}
        conversation_history.append(conversation_entry)
        
        # Insert into MongoDB
        history_collection.insert_one(conversation_entry)
        
        return jsonify({'message': formatted_response})
    except Exception as e:
        print(f"Error in chat route: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/history', methods=['GET'])
def history():
    # Return only user messages to populate history list from MongoDB
    history_entries = history_collection.find({}, {"_id": 0, "user": 1})
    return jsonify([entry for entry in history_entries])

@app.route('/history/<int:index>', methods=['GET'])
def history_detail(index):
    # Fetch detailed history from MongoDB based on index
    history_entries = list(history_collection.find({}, {"_id": 0}))  # Get all history without _id
    if 0 <= index < len(history_entries):
        return jsonify(history_entries[index])
    return jsonify({'error': 'Invalid index'}), 404

if __name__ == "__main__":
    app.run(debug=True)
