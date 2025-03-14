import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
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

# Function to Generate OpenAI Embeddings and Store in FAISS
def store_in_faiss(chunks, faiss_path="faiss_index"):
    """Generates OpenAI embeddings and stores them in a FAISS vector database."""
    embedding_model = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(faiss_path)
    print(f"✅ FAISS Index Created & Saved at {faiss_path}")
    return vectorstore

# Function to Perform Similarity Search
# def search_faiss(vectorstore, query, top_k=3):
#     """Performs a similarity search in FAISS and returns top matching results."""
#     retrieved_docs = vectorstore.similarity_search(query, k=top_k)
#     print("\n🔍 **Top Relevant Passages:**")
#     for i, doc in enumerate(retrieved_docs):
#         print(f"\nResult {i+1}:\n{doc.page_content}")  # Show first 500 chars
#     return retrieved_docs

# Main Function to Run the Pipeline
def main():
    # Ask user for the PDF file path
    pdf_path = input("📂 Enter the path of the PDF file to process: ")
    
    # Check if the file exists
    if not os.path.exists(pdf_path):
        print("❌ Error: The file does not exist. Please check the path and try again.")
        return

    faiss_path = "vector_db"

    # Load and process the PDF
    documents = load_pdf(pdf_path)
    if not documents:
        return

    # Split text into chunks
    text_chunks = split_text(documents)

    # Store in FAISS
    vectorstore = store_in_faiss(text_chunks, faiss_path)

    # # Perform similarity search
    # query = input("🔍 Enter your search query: ")
    # search_faiss(vectorstore, query)


if __name__ == "__main__":
    main()