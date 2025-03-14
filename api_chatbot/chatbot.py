from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

# Function to Load FAISS Vector Store
def load_vector_store(faiss_path="api_chatbot/vector_db"):
    """Loads the FAISS vector store from disk."""
    embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")
    vector_store = FAISS.load_local(
        faiss_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True # Required for loading from disk
    )
    print("✅ FAISS Vector Store Loaded!")
    return vector_store

# Function to Create a Conversational Chain
def create_conversation_chain(vector_store, llm_model="gpt-4o-mini"):
    """Creates a conversation chain using OpenAI LLM and FAISS vector store."""
    llm = ChatOpenAI(model_name=llm_model, temperature=0.8)  # Create LLM Model
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)  # Store conversation history
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

        response = conversation_chain({"question": user_question})
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