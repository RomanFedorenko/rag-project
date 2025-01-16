from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.prompt_service import PromptService

# Create your views here.
class PromptView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = PromptService(prompt)
        response = service.process_prompt()

        return Response({'message': response}, status=status.HTTP_200_OK)
