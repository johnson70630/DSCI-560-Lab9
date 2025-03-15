import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS

load_dotenv()

# Function to Load PDF and Extract Text
def load_pdf(pdf_path):
    """Loads a PDF file and extracts its text using LangChain's PyMuPDFLoader."""
    try:
        loader = PyMuPDFLoader(pdf_path)
        documents = loader.load()
        print(f"✅ Loaded {len(documents)} pages from {pdf_path}")
        return documents
    except Exception as e:
        print(f"❌ Error loading PDF: {e}")
        return None

# Function to Split Text into Chunks
def split_text(documents, chunk_size=500, chunk_overlap=50):
    """Splits extracted text into smaller overlapping chunks for better embeddings."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(documents)
    print(f"✅ Split text into {len(chunks)} chunks.")
    return chunks

# Function to Generate Hugging Face Embeddings and Store in FAISS
def store_in_faiss(chunks, faiss_path="vector_db_open_source"): #changed the default faiss path
    """Generates Hugging Face embeddings and stores them in a FAISS vector database."""
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(faiss_path)
    print(f"✅ FAISS Index Created & Saved at {faiss_path}")
    return vectorstore


def process_pdfs(pdf_folder, faiss_path="vector_db"):
    """Processes all PDFs in a folder, extracts text, chunks it, and stores embeddings."""
    pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    if not pdf_files:
        return "No PDF files found."

    # Load and process PDFs
    documents = []
    for pdf in pdf_files:
        docs = load_pdf(pdf)
        if docs:
            documents.extend(docs)

    # Split text into chunks
    text_chunks = split_text(documents)

    # Store embeddings in FAISS
    store_in_faiss(text_chunks, faiss_path)

    return "PDFs processed successfully!"





# Main Function to Run the Pipeline
def main():
    # Ask user for the PDF file path
    pdf_path = input("📂 Enter the path of the PDF file to process: ")

    # Check if the file exists
    if not os.path.exists(pdf_path):
        print("❌ Error: The file does not exist. Please check the path and try again.")
        return

    faiss_path = "vector_db_open_source" 

    # Load and process the PDF
    documents = load_pdf(pdf_path)
    if not documents:
        return

    # Split text into chunks
    text_chunks = split_text(documents)

    # Store in FAISS
    vectorstore = store_in_faiss(text_chunks, faiss_path)

if __name__ == "__main__":
    main()