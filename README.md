# DSCI-560-Lab9

## api_chatbot

This Python script extracts text from a PDF file, generates embeddings using OpenAI’s embedding model, and stores them in a FAISS vector database for fast similarity search. Users can search for relevant content from the document using natural language queries.

## Dependencies

Before running the script, ensure you have installed the required dependencies:

```
pip install langchain_community langchain_openai langchain_text_splitters python-dotenv faiss-cpu pymupdf tiktoken 
```

## How to Run the Script

1. Run the script
```
python api_chatbot/dataprocessing.py
```

2. Enter the PDF file path when prompted

the filepath of the default doc is `raw_data/Ads_cookbook.pdf`

## Output Files

- FAISS index stored in vector_db/ for future searches.
- Extracted text is processed and embedded in vector format.
