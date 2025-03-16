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


---

## API Chatbot (Open Source LLM Version)

These Python scripts (`data_preprocessing_os_ver.py` & `chatbot_os_ver.py`) extract text from a PDF file, generate embeddings using an open-source embedding model, and store them in a FAISS vector database for fast similarity search. Users can search for relevant content from the document using natural language queries.
  
### Setup

#### 1. Install Required Dependencies

Ensure you have the necessary dependencies installed using the following command:

```bash
pip install langchain langchain-huggingface langchain-community faiss-cpu python-dotenv llama-cpp-python
```
*To set up `llama-cpp-python`, please search for instruction online*

#### 2. Download the LlamaCpp Model

You'll need to download the specific LlamaCpp model you want to use and store it in the `models/` directory. 

For example, you can download the `qwq-32b-q4_k_m.gguf` model from [HuggingFace](https://huggingface.co/Qwen/QwQ-32B-GGUF/tree/main) and place it in the `models/` directory. 

Note: Due to the model's large size, it cannot be uploaded to GitHub directly.

### Running the Scripts

#### Step 1: Run the Data Processing Script

The `data_processing_os_ver.py` script processes a PDF file, generates embeddings, and stores them in a FAISS index for future search.

To run the script:

```bash
python api_chatbot/data_processing_os_ver.py
```

You will be prompted to enter the file path of the PDF document.

- Default document: `raw_data/Ads_cookbook.pdf`

#### Step 2: Output Files

- **FAISS Index**: Stored in the `vector_db/` folder for future similarity searches.
- **Extracted Text**: Processed and stored as embeddings in vector format.

#### Step 3: Run the Chatbot Script

Once the FAISS vector store is ready, you can run the chatbot to start interacting with the document.

To start the chatbot:

```bash
python api_chatbot/chatbot_os_ver.py
```

You can then enter your questions, and the chatbot will retrieve relevant answers from the document.

### Example Interaction

```
📝 You: What is the main topic of the document?
🤖 AI: The main topic of the document is circuit design using Keysight EEsof EDA Advanced Design System (ADS). Specifically, it details the process of creating a workspace and schematic designs within this software environment. Additionally, there are mentions related to RF system integration into DSP designs using Ptolemy as the end-to-end simulator...
```

```
📝 You: Summarize the pdf.
🤖 AI: Okay, the user wants me to summarize a PDF. The provided context includes several figures (like Figures 339–345 and others)) and some technical details about Yield Analysis.

First, I need to figure out what's in this PDF based on the given context. It seems ...
```

```
📝 You: exit
👋 Goodbye!
```

---

## Web Design

Run `app.py` in `api_chatbox` folder. You will see something like `* Running on http://127.0.0.1:5000` in terminal output. Paste this url on your local browser and you'd be able to upload pdf and interact with the chatbot on the web.



