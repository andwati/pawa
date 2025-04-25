import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Layout from '../components/Layout';
import SummaryDisplay from '../components/SummaryDisplay';

const SummaryPage = () => {
    const router = useRouter();
    const { query } = router;
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (query.documentId) {
            fetch(`/api/summarize/${query.documentId}`)
                .then((response) => response.json())
                .then((data) => {
                    setSummary(data.summary);
                    setLoading(false);
                })
                .catch((error) => {
                    console.error('Error fetching summary:', error);
                    setLoading(false);
                });
        }
    }, [query.documentId]);

    if (loading) {
        return (
            <Layout>
                <div className="flex justify-center items-center h-screen">
                    <p>Loading summary...</p>
                </div>
            </Layout>
        );
    }

    return (
        <Layout>
            <div className="p-4">
                <h1 className="text-2xl font-bold mb-4">Document Summary</h1>
                {summary ? (
                    <SummaryDisplay summary={summary} />
                ) : (
                    <p>No summary available.</p>
                )}
            </div>
        </Layout>
    );
};

export default SummaryPage;