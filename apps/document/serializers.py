from rest_framework import serializers

from apps.document.helpers import DocumentHelper
from apps.document.models import Document, DocumentEmbedding


class DocumentIngestionSerializer(serializers.ModelSerializer):
    """
    Serializer for ingesting documents.
    Validates the input data for the POST request.
    Generates embeddings for the document content using the GenerateEmbedding
    utility and stores them in the database.
    """

    content = serializers.CharField(required=True)

    class Meta:
        model = Document
        fields = ("id", "title", "content")

    def create(self, validated_data):
        """
        Create a new document instance  and its associated embedding.
        Args:
            validated_data (dict): Validated data for creating a document.
        Returns:
            Document: The created document instance.
        """
        # Generates embeddings
        embedding = DocumentHelper.generate_embedding(validated_data["content"])
        document_instance = self.Meta.model.objects.create(**validated_data)
        DocumentEmbedding.objects.create(
            document=document_instance, embedding=embedding
        )
        return document_instance


class QuestionAnswerSerializer(serializers.Serializer):
    """
    Serializer for answering questions.
    Validates the input data for the POST request.
    Retrieves the answer for the given question using the GetAnswer utility.
    """

    question = serializers.CharField(required=True)

    def get_answer(self):
        """
        Retrieve the answer for the given question.
        Returns:
            dict: A dictionary containing the answer to the question.
        """
        # Get answer for the question
        validated_data = self.validated_data
        answer = DocumentHelper.get_answer(validated_data["question"])
        return {"answer": answer}


class DocumentSelectionSerializer(serializers.Serializer):
    """
    Serializer for selecting documents.
    Validates the input data for the POST request.
    Updates the selected documents based on the provided IDs.
    """

    document_ids = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Document.objects.all()),
        required=True,
    )

    def update_selected_documents(self):
        """
        Update the selected documents based on the provided IDs.
        Args: None
        Returns:
            dict: A dictionary containing a success message.
        """
        validated_data = self.validated_data
        document_ids = validated_data["document_ids"]
        document_ids = [document.id for document in document_ids]
        # Filter the documents based on the provided IDs
        Document.objects.filter(id__in=document_ids).update(is_selected_for_rag=True)
        return {"message": "Document selection successful"}
