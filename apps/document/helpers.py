"""
This module contains the DocumentHelper class which is used to generate
embeddings for a given document
and get an answer for a given question.
"""


class DocumentHelper:
    """
    Class to generate embeddings for a given document.

    """

    @staticmethod
    def generate_embedding(param):
        """
        Generate embeddings for the given document content.
        Args:
            param (str): The document content.
        Returns:
            list: A list of embeddings for the document.
        """
        return []

    @staticmethod
    def get_answer(question):
        """
        Get an answer for the given question.
        Args:
            question (str): The question to be answered.
        Returns:
            str: The answer to the question.
        """
        return "This is a sample answer"
