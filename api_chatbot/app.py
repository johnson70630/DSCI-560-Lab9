from flask import Flask, render_template, request, jsonify
import os
# from chatbot import ask_chatbot  # Import chatbot function
# from data_processing import process_pdfs  # Import PDF processing function
from chatbot_os_ver import ask_chatbot  # Import chatbot function
from data_preprocessing_os_ver import process_pdfs  # Import PDF processing function

app = Flask(__name__)

UPLOAD_FOLDER = "uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdfs():
    files = request.files.getlist("files")
    for file in files:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    
    process_pdfs(UPLOAD_FOLDER)  # Process PDFs into embeddings
    return jsonify({"message": "PDFs uploaded and processed successfully!"})

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"]
    answer = ask_chatbot(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
