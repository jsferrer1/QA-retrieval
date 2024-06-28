# Q&A AI Retrieval System

## Getting started

Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Downloading Llama3 and using it:
```bash
ollama run llama3
```

Serving the Llama3 locally:
```bash
ollama serve
```

Run the following command to install the required libraries.
```
pip install -r requirements.txt
```

## Developing the AI Application Locally

Run the following `store_vectore.ipynb` for building the vector store and testing the code.

Then, run:
```bash
python AI_app.py
```
Output:
```bash
Question: Who is John?

Answer: According to the context, John is a person who answered questions from a crowd, teachers, tax collectors, and soldiers. He gave advice on sharing resources, not collecting more than required, and being honest in their dealings.

Question:
```