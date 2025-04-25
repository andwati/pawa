# Legal Document Summarizer Frontend

This project is a frontend application for the Legal Document Summarizer, built using Next.js and styled with Tailwind CSS. It allows users to upload legal documents in PDF or TXT format and receive summarized content from the backend API.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd legal-document-summarizer/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then, run the following command to install the required packages:
   ```bash
   npm install
   ```

3. **Run the Development Server**
   Start the Next.js development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:3000`.

## File Structure

- **public/**: Contains static files such as images and the favicon.
- **src/**: Contains the main application code.
  - **components/**: Reusable React components.
    - `FileUpload.tsx`: Component for uploading documents.
    - `SummaryDisplay.tsx`: Component for displaying the summary.
    - `Layout.tsx`: Layout component for consistent structure.
  - **pages/**: Next.js pages.
    - `index.tsx`: Main landing page.
    - `summary.tsx`: Page for displaying the document summary.
  - **styles/**: Contains global styles and Tailwind CSS configuration.
  - **utils/**: Utility functions for API calls.

## Tailwind CSS

This project uses Tailwind CSS for styling. You can customize the styles in the `tailwind.config.js` file.

## API Integration

The frontend communicates with the backend FastAPI application to send document data and receive summaries. Ensure that the backend is running and accessible.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.