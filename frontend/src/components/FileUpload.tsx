import React, { useState } from 'react';

const FileUpload: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [summary, setSummary] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            setFile(event.target.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!file) return;

        setLoading(true);
        setError(null);
        setSummary(null);

        const formData = new FormData();
        formData.append('document', file);

        try {
            const response = await fetch('/api/v1/summarize', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to summarize document');
            }

            const data = await response.json();
            setSummary(data.summary);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col items-center">
            <input
                type="file"
                accept=".pdf,.txt"
                onChange={handleFileChange}
                className="mb-4"
            />
            <button
                onClick={handleUpload}
                className="bg-blue-500 text-white px-4 py-2 rounded"
                disabled={loading}
            >
                {loading ? 'Uploading...' : 'Upload Document'}
            </button>
            {error && <p className="text-red-500 mt-2">{error}</p>}
            {summary && <p className="mt-4">{summary}</p>}
        </div>
    );
};

export default FileUpload;