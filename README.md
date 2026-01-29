Website-Based AI Chatbot
Overview
This project is a Website-Based AI Chatbot that allows users to ask questions about a website and receive answers strictly based on that website’s content. The system follows a Retrieval-Augmented Generation (RAG) approach to ensure accurate, context-aware, and hallucination-free responses.
The chatbot works only with static HTML websites. JavaScript-heavy or dynamically rendered websites (such as Google or YouTube) are intentionally not supported.
________________________________________
What This Project Does
1.	Accepts a website URL from the user
2.	Crawls and extracts meaningful HTML content from the website
3.	Converts the content into vector embeddings
4.	Stores embeddings in ChromaDB
5.	Generates a short summary of the website after indexing
6.	Allows users to ask questions related only to the indexed website
7.	Returns answers strictly based on the website content
If the answer is not found on the website, the chatbot clearly responds: > “The answer is not available on the provided website.”

________________________________________
Technologies Used
•	Python 3
•	Streamlit – for the user interface
•	Requests & BeautifulSoup – for web crawling
•	Sentence Transformers – for embedding generation
•	ChromaDB – vector database
•	Groq LLM – for answer generation
•	python-dotenv – environment variable management

________________________________________
Project Structure
Humanli/
│── app.py            # Main Streamlit application
│── crawler.py        # Website crawling and content extraction
│── chunker.py        # Text chunking logic
│── vectorstore.py    # ChromaDB storage and retrieval
│── rag.py            # RAG logic (Q&A and summary)
│── requirements.txt  # Project dependencies
│── README.md         # Project documentation
│── .gitignore        # Git ignore file

________________________________________
Setup and Installation (Step-by-Step)
Step 1: Clone the Repository
git clone <https://github.com/MayankKunwarSingh/Website_Based_Chatbot>
cd Humanli

________________________________________
Step 2: Create a Virtual Environment
python -m venv venv
Activate the virtual environment:
•	Windows:
venv\Scripts\activate

•	Linux / macOS:
source venv/bin/activate
________________________________________
Step 3: Install Required Dependencies
pip install -r requirements.txt
________________________________________
Step 4: Set Up Environment Variables
Create a .env file in the project root (this file should NOT be pushed to GitHub):
GROQ_API_KEY=your_groq_api_key_here
On deployment platforms like Vercel, set this key using the platform’s Environment Variables settings instead of using .env.
________________________________________
Running the Project
Start the Streamlit application using:
streamlit run app.py
Open your browser and go to:
http://localhost:8501
________________________________________
How to Use the Chatbot
1.	Enter a static HTML website URL
2.	Click Index Website
3.	View the automatically generated website summary
4.	Ask questions related to the website content
Example Websites That Work
•	https://en.wikipedia.org/wiki/Artificial_intelligence
•	https://www.python.org
•	https://docs.python.org/3/
Websites That Are Not Supported
•	Google
•	YouTube
•	Instagram
•	LinkedIn
(These websites use JavaScript rendering and do not expose meaningful HTML content.)
________________________________________
Important Notes
•	The chatbot answers questions only from website content
•	No external knowledge or internet search is used
•	Chat history is stored only for the current session
•	The project is designed to avoid hallucinations
________________________________________
License
This project is licensed under the MIT License.
________________________________________
Conclusion
This project demonstrates a clean and practical implementation of a Retrieval-Augmented Generation chatbot using modern AI tools. It focuses on correctness, simplicity, and ethical content handling, making it suitable for academic evaluation, technical assessments, and portfolio presentation.

Build by Mayank Raj
