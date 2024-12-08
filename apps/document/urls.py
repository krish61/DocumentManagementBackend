from django.urls import path

from apps.document.views import (
    DocumentIngestionAPIView,
    QuestionAnswerApiView,
    DocumentSelectionAPIView,
)

app_name = "document"
urlpatterns = [
    path(
        "ingest-document/", DocumentIngestionAPIView.as_view(), name="ingest_document"
    ),
    path("qa/", QuestionAnswerApiView.as_view(), name="question_answer"),
    path(
        "select-documents/", DocumentSelectionAPIView.as_view(), name="select_documents"
    ),
]
