from django.db import models


class Document(models.Model):
    """
    Model representing a document.
    Stores the title, content, and creation date of the document.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_selected_for_rag = models.BooleanField(default=False)


class DocumentEmbedding(models.Model):
    """
    Model representing embeddings for a document.
    Stores the document, embedding, and creation date of the embedding.
    """

    document = models.ForeignKey(
        Document, related_name="embeddings", on_delete=models.CASCADE
    )
    # Store embeddings as JSON
    embedding = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
