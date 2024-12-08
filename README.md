# Document API

This project provides an API for managing documents, generating embeddings for document ingestion, and enabling

retrieval-based Q&A using RAG (Retrieval-Augmented Generation). The backend is built using Django Rest Framework.

## Setup

Follow these steps to set up the project:

### Prerequisites

- Python 3.12+
- Django 5.1+
- Django Rest Framework
- python-dotenv (for environment variable management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/krish61/DocumentManagementBackend.git
   cd DocumentManagmentBackend
   ```
2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in the project root and define environment variables:
    ```
    DEBUG = ***
    DJANGO_SECRET_KEY = "******"
    DATABASE_NAME = "*******"
    DATABASE_USER = "*******"
    DATABASE_PASSWORD = "******"
    DATABASE_HOST = "*****"
    ```
5. Run migrations to set up the database:
    ```bash
   make migrate
   ```
6. Start the Django development server:
    ```bash
   make
   ```

## API Endpoints

### 1. **Document Ingestion API**

- **Endpoint**: `api/ingest-document/`
- **Method**: `POST`
- **Description**: Accepts document data, generates embeddings using a large language model (LLM), and stores them for
  future retrieval.
- **Request Body**:
  ```json
  {
    "title": "Document Title",
    "content": "This is the content of the document."
  }
  ```
- **Response**:
  ```json
  {
    "id":1,
    "title": "Document Title",
    "content": "This is the content of the document"
  }
  ```

### 2. **Q&A API**

- **Endpoint**: `api/qa/`
- **Method**: `POST`
- **Description**: Accepts user questions, retrieves relevant document embeddings, and generates answers based on the
  retrieved content using RAG.
- **Request Body**:
  ```json
  {
    "question": "What is the purpose of document ingestion?"
  }
  ```
- **Response**:
  ```json
  {
    "answer": "This is a sample answer"
  }
  ```

### 3. **Document Selection API**

- **Endpoint**: `api/select-documents/`
- **Method**: `POST`
- **Description**: Allows users to specify which documents should be considered in the RAG-based Q&A process.
- **Request Body**:
  ```json
  {
    "document_ids": [1, 2, 3]
  }
  ```
- **Response**:
  ```json
  {
    "message": "Document selection successful"
  }
  ```
