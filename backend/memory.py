import chromadb
from chromadb.config import Settings
import uuid

class ResearchMemory:
    def __init__(self, collection_name="google_research_memory"):
        """
        Initialize ChromaDB client and collection.
        """
        self.client = chromadb.Client(Settings(
            is_persistent=False
        ))
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_documents(self, documents, metadatas):
        """
        Add documents to the ChromaDB collection.
        
        Args:
            documents (list): List of text strings (snippets).
            metadatas (list): List of dictionaries containing metadata (e.g., source link).
        """
        ids = [str(uuid.uuid4()) for _ in range(len(documents))]
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Added {len(documents)} documents to memory.")

    def query_documents(self, query_text, n_results=5):
        """
        Retrieve relevant documents based on a query.
        
        Args:
            query_text (str): The query string.
            n_results (int): Number of results to return.
            
        Returns:
            dict: Query results containing documents and metadatas.
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def clear_memory(self):
        """
        Deletes the collection to reset memory.
        """
        try:
            self.client.delete_collection(self.collection.name)
            self.collection = self.client.create_collection(self.collection.name)
            print("Memory cleared.")
        except Exception as e:
            print(f"Error clearing memory: {e}")

if __name__ == "__main__":
    # Test the memory module
    memory = ResearchMemory()
    
    # Mock data
    docs = ["AI is transforming healthcare.", "Machine learning helps in diagnosis."]
    meta = [{"source": "example.com"}, {"source": "test.com"}]
    
    memory.add_documents(docs, meta)
    
    results = memory.query_documents("healthcare AI")
    print("Query Results:", results)
