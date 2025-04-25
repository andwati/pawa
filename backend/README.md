# Legal Document Summarizer Backend

This project is a legal document summarizer that utilizes FastAPI for the backend and Next.js for the frontend. The backend processes document uploads in PDF or TXT format and interacts with the Gemini API to generate summaries.

## Project Structure

- **app**: Contains the main application code.
  - **api**: Contains the API versioning and endpoints.
    - **v1**: Version 1 of the API.
      - **endpoints**: Contains the endpoint definitions.
        - `summarize.py`: Endpoint for summarizing documents.
      - `__init__.py`: Initializes the API version 1 module.
  - **core**: Contains configuration settings for the application.
    - `config.py`: Configuration settings, including API keys and environment variables.
  - **models**: Contains data models.
    - `document.py`: Defines the Document model for uploaded documents.
  - **schemas**: Contains Pydantic schemas for request and response validation.
    - `summary.py`: Defines the Summary schema for the API response.
  - **services**: Contains service functions for external API interactions.
    - `gemini_api.py`: Functions to interact with the Gemini API.
  - `main.py`: Entry point of the FastAPI application.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd legal-document-summarizer/backend
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application**:
   ```
   uvicorn app.main:app --reload
   ```

4. **Access the API documentation**:
   Open your browser and navigate to `http://localhost:8000/docs` to view the interactive API documentation.

## Usage

- Upload a PDF or TXT document to the `/api/v1/summarize` endpoint using a POST request.
- The response will contain the summarized text of the document.

## Dependencies

- FastAPI
- Uvicorn
- Pydantic
- Any additional libraries required for the Gemini API interaction.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.