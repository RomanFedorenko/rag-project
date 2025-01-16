class RetrievalService:
    def __init__(self, prompt):
        self.prompt = prompt

    def retrieve_documents(self):
        documents = self.search_documents(self.prompt)
        return documents

    def search_documents(self, prompt):
        return ["Document 1 content related to the prompt", "Document 2 content"]
