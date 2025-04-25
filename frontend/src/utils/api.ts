import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export const summarizeDocument = async (file: File) => {
    const formData = new FormData();
    formData.append('document', file);

    try {
        const response = await axios.post(`${API_URL}/summarize`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error summarizing document:', error);
        throw error;
    }
};