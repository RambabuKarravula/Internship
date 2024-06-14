# RAG-Powered Chatbot for PDF Question Answering
Project Description
This project involves creating a Retrieval-Augmented Generation (RAG) powered chatbot capable of answering questions based on a provided PDF document. The chatbot is designed to interact with users, understand their queries, and provide accurate and contextually relevant answers using the contents of the PDF. The assignment entails constructing a dataset for testing, measuring the model's accuracy, and striving to enhance this accuracy through various methods.

# Dataset Construction
Thought Process:
To evaluate the chatbot effectively, I constructed a diverse dataset encompassing various types of queries derived from the PDF document. The chosen PDF, a policy booklet from Churchill, covers comprehensive details about car insurance policies. Here's how I approached the dataset construction:

# PDF Analysis:

Understanding Content: I thoroughly reviewed the PDF to understand its structure, sections, and the type of information it contains.
Identifying Key Sections: Key sections such as policy terms, coverage details, claim procedures, exclusions, and FAQs were identified for creating diverse queries.
Query Creation:

Diverse Topics: Queries were created to cover different sections and topics within the PDF, ensuring that no single section was over-represented.
Complexity Variation: The queries ranged from simple fact-based questions to more complex scenario-based questions.
Real-World Relevance: Practical, real-world questions that a user might ask about their car insurance policy were included.
Response Extraction:

Accurate Responses: Responses were extracted directly from the PDF to ensure accuracy.
Contextual Relevance: The context of the queries was considered to provide precise and relevant answers.
Sample Dataset:
The dataset comprises 30 query-response pairs. Here’s an example of a few entries:

# Query	Response
What is the policy number for accidental damage coverage?	The policy number for accidental damage coverage is detailed in Section 3.1 on page 15.
How do I file a claim for theft?	To file a claim for theft, you need to contact our claims department immediately at the number provided on page 2, and follow the steps outlined in Section 5.2 on page 22.
What is covered under fire and theft insurance?	Fire and theft insurance covers damage caused by fire, lightning, explosion, theft, or attempted theft as detailed in Section 4 on page 17.
Is windscreen damage covered under my policy?	Yes, windscreen damage is covered under your policy as outlined in Section 6 on page 23.
Comprehensive Dataset Explanation:
This dataset is comprehensive because it:

Covers Multiple Sections: Ensures that various sections of the PDF are represented, giving a holistic view of the document.
Includes Diverse Query Types: Ranges from straightforward fact-based queries to intricate procedural questions, testing the chatbot's versatility.
Represents Real-World Scenarios: Mimics real questions that users might ask, ensuring practical applicability and relevance.
Evaluation Metrics
Thought Process:
Selecting appropriate evaluation metrics is crucial to accurately measure the chatbot's performance. I chose the following metrics:

Accuracy: Measures the proportion of correct answers provided by the chatbot.

Reason**: Provides a clear indication of how often the chatbot gives the right answer.
F1 Score: Considers both precision and recall, giving a balanced view of the chatbot's performance.

Reason: Accounts for both the relevance and completeness of the responses.
BLEU Score: Measures the similarity between the chatbot's response and the reference response.

Reason: Useful for evaluating the quality of generated text in NLP tasks.
Metric Application:
These metrics were applied to the query-response pairs in the dataset to assess the chatbot’s performance.

# Improving Accuracy
# Thought Process:
To enhance the chatbot’s accuracy, I implemented several strategies:

# Fine-Tuning the Model:

Pre-trained Models: Leveraged pre-trained models and fine-tuned them using the dataset to improve domain-specific understanding.
Hyperparameter Optimization: Experimented with different model parameters to find the optimal settings.
Enhanced Text Processing:

Text Preprocessing: Improved text preprocessing steps to ensure cleaner input data.
Contextual Embeddings: Used contextual embeddings to capture the meaning of queries more effectively.
Retrieval-Augmentation:

Efficient Retrieval: Enhanced the retrieval mechanism to ensure that the most relevant sections of the PDF are used for generating responses.
Augmentation Techniques: Incorporated techniques like data augmentation to expand the training dataset and improve model robustness.
User Feedback Integration:

Iterative Testing: Continuously tested the chatbot with new queries and refined it based on feedback.
User Interactions: Collected feedback from potential users to identify common issues and areas for improvement.
