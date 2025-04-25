import React from 'react';

interface SummaryDisplayProps {
    summary: string | null;
}

const SummaryDisplay: React.FC<SummaryDisplayProps> = ({ summary }) => {
    return (
        <div className="p-4 border rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-2">Document Summary</h2>
            {summary ? (
                <p className="text-gray-700">{summary}</p>
            ) : (
                <p className="text-gray-500">No summary available. Please upload a document.</p>
            )}
        </div>
    );
};

export default SummaryDisplay;