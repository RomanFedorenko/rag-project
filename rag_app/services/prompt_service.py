from .retrieval_service import RetrievalService
from .llm_service import LLMService


class PromptService:
    def __init__(self, prompt):
        self.prompt = prompt

    def process_prompt(self):
        retrieval_service = RetrievalService(self.prompt)
        documents = retrieval_service.retrieve_documents()

        llm_service = LLMService(documents, self.prompt)
        response = llm_service.generate_response()

        return response