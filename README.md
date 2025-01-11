
# 🏥 First Aid Assistant Chatbot

A Flask-based AI chatbot that provides first aid assistance using LangChain, OpenAI GPT-4o-mini, MongoDB, and Tailwind CSS. The chatbot can process PDF first-aid manuals, store conversation history, and deliver context-aware responses

# 🏗️ Project Overview
```
Conversational AI: Uses OpenAI's GPT-4o-mini for intelligent first-aid guidance.

PDF Knowledge Extraction: Parses first-aid manuals for reference.

Chat History Persistence: Stores and retrieves past conversations using MongoDB.

Web-Based Interface: Built with Flask & Tailwind CSS.

Fast & Scalable: Uses LangChain for structured LLM interactions.
```

# 🛠️ Installation & Setup
```
1️⃣ Clone the Repository
git clone https://github.com/yourusername/first-aid-chatbot.git
cd first-aid-chatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Setup Environment Variables
Create a .env file and add:
OPENAI_API_KEY=your-openai-api-key
MONGO_URI=your-mongodb-connection-string

4️⃣ Run the Flask App
python app.py
```

# 📂 Project Structure
> First-Aid Chatbot Project
```tree
first-aid-chatbot/
│── app.py                 # Main Flaskapplication
│── templates/
│   ├── index.html         # Web UI
│── ll.py                  # LangChain conversation logic
│── First_aid.pdf          # PDF text extraction
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

```
# 📖 Usage
```
1.Upload a first-aid PDF manual.

2.Ask the chatbot first-aid-related questions.

3.Receive AI-generated responses based on the manual.

3.View past chat history.
```
# 🏗️ Future Improvements
```
✅ Mobile app integration

✅ More first-aid knowledge sources
```

# ⭐ Acknowledgments

This project was developed as part of our 7th Semester Computer Science Project. Special thanks to our Teacher our mentor  Sir Hammas U Rehman for such excepational teaching which helped me and my  colleagus in developing Chatbots.  I also want to extend my gratitue to Timoor Khan for being my teammate his contribution toward this project is truly remarkable his skills in flask and formatting chatbot responses are truly commendable.
```
# 📜 License
```

This project is licensed under the MIT License.

# ⭐ Give this repository a star if you found it helpful!
# Author 
1. Muhammad Umair 
2. Timoor Khan









