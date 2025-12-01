class ResearchMemory:
    def __init__(self, collection_name="google_research_memory"):
        """
        Initialize simple in-memory storage.
        """
        self.documents = []
        self.metadatas = []

    def add_documents(self, documents, metadatas):
        """
        Add documents to the in-memory list.
        """
        self.documents.extend(documents)
        self.metadatas.extend(metadatas)
        print(f"Added {len(documents)} documents to memory.")

    def query_documents(self, query_text, n_results=5):
        """
        Retrieve relevant documents. 
        For this lightweight version, we simply return the most recent documents
        or all of them if fewer than n_results.
        """
        # Simple implementation: return the last n_results documents
        # In a real app, we could do TF-IDF or simple keyword matching here.
        
        count = min(len(self.documents), n_results)
        return {
            'documents': [self.documents[:count]],
            'metadatas': [self.metadatas[:count]]
        }

    def clear_memory(self):
        """
        Clear memory.
        """
        self.documents = []
        self.metadatas = []
        print("Memory cleared.")

if __name__ == "__main__":
    # Test the memory module
    memory = ResearchMemory()
    
    # Mock data
    docs = ["AI is transforming healthcare.", "Machine learning helps in diagnosis."]
    meta = [{"source": "example.com"}, {"source": "test.com"}]
    
    memory.add_documents(docs, meta)
    
    results = memory.query_documents("healthcare AI")
    print("Query Results:", results)
