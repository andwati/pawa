import { useState } from 'react';
import FileUpload from '../components/FileUpload';
import SummaryDisplay from '../components/SummaryDisplay';
import Layout from '../components/Layout';

const Home = () => {
  const [summary, setSummary] = useState<string | null>(null);

  const handleSummaryUpdate = (newSummary: string) => {
    setSummary(newSummary);
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-4">Legal Document Summarizer</h1>
      <FileUpload onSummaryUpdate={handleSummaryUpdate} />
      {summary && <SummaryDisplay summary={summary} />}
    </Layout>
  );
};

export default Home;