"""
This module contains test cases for the document app.
It includes tests for the following functionalities:
- Document ingestion
- Question answering
- Document selection
"""

from rest_framework.test import APITestCase

from django.urls import reverse

from rest_framework import status

from apps.document.models import Document


class DocumentIngestTestCase(APITestCase):
    """
    Test case for document ingestion.
    """

    url = reverse("document:ingest_document")
    data = {
        "title": "Test Document",
        "content": "This is a test document content.",
    }

    def test_document_ingest_api(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().title, "Test Document")

    def test_document_ingest_api_without_title(self):
        data = self.data.copy()
        del data["title"]
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Document.objects.count(), 0)

    def test_document_ingest_api_without_content(self):
        data = self.data.copy()
        del data["content"]
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Document.objects.count(), 0)


class QuestionAnswerTestCase(APITestCase):
    """
    Test case for question answering.
    """

    url = reverse("document:question_answer")
    data = {
        "question": "What is the purpose of this document?",
    }

    def test_question_answer_api(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data["answer"])
        self.assertEqual(response.data["answer"], "This is a sample answer")

    def test_question_answer_api_without_question(self):
        data = self.data.copy()
        del data["question"]
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DocumentSelectionTestCase(APITestCase):
    """
    Test case for document selection.
    """

    url = reverse("document:select_documents")

    def setUp(self):
        Document.objects.bulk_create(
            [
                Document(
                    title="Test Document", content="This is a test document content."
                ),
                Document(
                    title="Test Document", content="This is a test document content."
                ),
                Document(
                    title="Test Document", content="This is a test document content."
                ),
            ]
        )

        self.data = {
            "document_ids": list(Document.objects.values_list("id", flat=True)),
        }

    def test_document_selection_api(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Document selection successful")

    def test_document_selection_api_without_document_ids(self):
        data = self.data.copy()
        del data["document_ids"]
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_document_selection_api_with_invalid_document_ids(self):
        data = self.data.copy()
        data["document_ids"] = [1, 2, 3, 4]
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
