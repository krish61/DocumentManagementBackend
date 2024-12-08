from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import (
    DocumentIngestionSerializer,
    QuestionAnswerSerializer,
    DocumentSelectionSerializer,
)


class DocumentIngestionAPIView(APIView):
    """
    View for ingesting documents and generating embeddings.
    Accepts POST requests with document data and generates embeddings.
    Stores the document and embedding in the database.
    """

    serializer_class = DocumentIngestionSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                serializer_data.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionAnswerApiView(APIView):
    """ "
    View for handling Q&A requests.
    Accepts POST requests with a question and uses RAG-based Q&A
    """

    serializer_class = QuestionAnswerSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            answer = serializer_data.get_answer()
            return Response(answer)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentSelectionAPIView(APIView):
    """
    View for selecting documents for Q&A.
    Accepts POST requests with a list of document IDs
    and marks them as selected for RAG-based Q&A.
    """

    serializer_class = DocumentSelectionSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.update_selected_documents()
            return Response({"message": "Document selection successful"})
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
