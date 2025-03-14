# DSCI-560-Lab9

## api_chatbot

This Python script extracts text from a PDF file, generates embeddings using OpenAI’s embedding model, and stores them in a FAISS vector database for fast similarity search. Users can search for relevant content from the document using natural language queries.

## Dependencies

Before running the script, ensure you have installed the required dependencies:

```
pip install langchain_community langchain_openai langchain_text_splitters python-dotenv faiss-cpu pymupdf tiktoken 
```

## Configuration

Set Up Your OpenAI API Key
- Create a .env file in the project directory
- Add your OpenAI API key

```
OPENAI_API_KEY=your_openai_api_key
```

## Run the data_processing.py

1. Run the script
```
python api_chatbot/data_processing.py
```

2. Enter the PDF file path when prompted

the filepath of the default doc is `raw_data/Ads_cookbook.pdf`

## Output Files

- FAISS index stored in vector_db/ for future searches.
- Extracted text is processed and embedded in vector format.

## Run the chatbot.py

1. Run the script

```
python api_chatbot/chatbot.py
```

2. Enter your question

```
📝 You: What is the main topic of the document?
🤖 AI: The document discusses...
```

3. Continue the conversation

```
📝 You: Tell me more about the conclusion.
🤖 AI: The conclusion states that...
```
4. Type 'exit' to quit

```
📝 You: exit
👋 Goodbye!
```

## Project Structure

```
api_chatbot/
│── chatbot.py              # Main chatbot script
│── vector_db/              # FAISS vector store directory
│── .env                    # OpenAI API Key (must be set)
│── requirements.txt         # Dependencies list
```