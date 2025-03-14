from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.llms import LlamaCpp
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

# Function to Load FAISS Vector Store
def load_vector_store(faiss_path="vector_db_open_source"):
    """Loads the FAISS vector store from disk."""
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
    vector_store = FAISS.load_local(
        faiss_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True  
    )
    print("✅ FAISS Vector Store Loaded!")
    return vector_store

# Function to Create a Conversational Chain
def create_conversation_chain(vector_store, model_path="models/qwq-32b-q4_k_m.gguf"):
    """Creates a conversation chain using LlamaCpp and FAISS vector store."""
    llm = LlamaCpp(model_path=model_path, n_ctx=512, n_batch=256)  
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, return_messages_when_empty=True)  
    conversation_chain = ConversationalRetrievalChain.from_llm(llm, vector_store.as_retriever(), memory=memory)
    print("✅ Conversation Chain Initialized!")
    return conversation_chain

# Function to Run Interactive Q&A Session
def chat_with_vector_db(conversation_chain):
    """Runs an interactive chat session with the user."""
    print("\n💬 AI Chatbot: Ask me anything! Type 'exit' to quit.\n")

    while True:
        user_question = input("📝 You: ")

        if user_question.lower() == "exit":
            print("👋 Goodbye!")
            break

        response = conversation_chain.invoke({"question": user_question})
        print(f"🤖 AI: {response['answer']}\n")

# Driver Function
def main():
    # Load FAISS vector store
    vector_store = load_vector_store()

    # Create conversation chain
    conversation_chain = create_conversation_chain(vector_store)

    # Start interactive chat
    chat_with_vector_db(conversation_chain)

if __name__ == "__main__":
    main()