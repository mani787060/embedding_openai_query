# OpenAI Text Embeddings & Semantic Querying

## 🧠 Project Overview
This repository demonstrates the technical implementation of **Text Embeddings** using OpenAI's API. While traditional search relies on keyword matching, embeddings allow for **Semantic Search**, where the system understands the underlying meaning and context of a query, even if the exact words don't match.

---

## 🛠️ Key Technical Implementations

### 1. Vector Generation
* **Embedding Models:** Utilizing `text-embedding-3-small` or `text-embedding-3-large`.
* **Dimension Control:** Implementing the `dimensions` parameter to optimize for storage and speed without losing semantic integrity.

### 2. Similarity Mathematics
* **Cosine Similarity:** Calculating the "distance" between vectors to find the most relevant matches.
* **Dot Product:** Implementing alternative scoring methods for high-dimensional space comparison.

### 3. Semantic Querying Pipeline
* **Input Normalization:** Cleaning and preparing text for vectorization.
* **Query Transformation:** Converting user natural language into a vector and searching against a local "knowledge base" (CSV/JSON).

### 4. Advanced Visualization (Optional)
* **Dimensionality Reduction:** Using **t-SNE** or **PCA** to project 1536-dimensional vectors into 2D/3D plots for cluster analysis.

---

## 💻 Tech Stack
* **Language:** Python
* **API:** OpenAI `embeddings` endpoint
* **Mathematics:** NumPy, SciPy (for distance metrics)
* **Visualization:** Matplotlib / Seaborn / Plotly

