# Legal Document Summarizer

This project is a web application designed to summarize legal documents using a FastAPI backend and a Next.js frontend styled with Tailwind CSS. The application allows users to upload documents in PDF or TXT format and receive a summarized version of the content.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using FastAPI and is responsible for handling document uploads and summarization. The key components include:

- **API Endpoints**: Located in `backend/app/api/v1/endpoints/summarize.py`, this file contains the endpoint for summarizing documents.
- **Configuration**: The configuration settings for the FastAPI application can be found in `backend/app/core/config.py`.
- **Models and Schemas**: The document model is defined in `backend/app/models/document.py`, and the summary schema is outlined in `backend/app/schemas/summary.py`.
- **Services**: The `backend/app/services/gemini_api.py` file contains functions to interact with the Gemini API for document summarization.
- **Main Application**: The entry point of the FastAPI application is in `backend/app/main.py`.

### Frontend

The frontend is built using Next.js and styled with Tailwind CSS. It provides a user-friendly interface for uploading documents and displaying summaries. Key components include:

- **File Upload**: The `FileUpload` component in `frontend/src/components/FileUpload.tsx` handles the file upload process.
- **Summary Display**: The `SummaryDisplay` component in `frontend/src/components/SummaryDisplay.tsx` shows the summarized text.
- **Layout**: The `Layout` component in `frontend/src/components/Layout.tsx` wraps the main application structure.
- **Pages**: The main landing page is located in `frontend/src/pages/index.tsx`, and the summary display page is in `frontend/src/pages/summary.tsx`.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies using npm:
   ```
   npm install
   ```
3. Start the Next.js application:
   ```
   npm run dev
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Use the file upload feature to select a PDF or TXT document.
3. Submit the document to receive a summarized version.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.