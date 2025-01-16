class LLMService:
    def __init__(self, documents, prompt):
        self.documents = documents
        self.prompt = prompt

    def generate_response(self):

        response = self.call_llm_api(self.documents, self.prompt)
        return response

    def call_llm_api(self, documents, prompt):
        return f"Generated response based on {prompt} and documents {documents}"
