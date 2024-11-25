# Repository: Search Engine Built from Scratch

This repository demonstrates the development of a **search engine from scratch** by implementing essential features such as **Scraping**, **Indexing**, and **Ranking** of documents. The ranking is achieved by calculating **TF-IDF weighted vectors** and measuring **pairwise cosine similarity**. Below, you will find an overview of the tasks completed and instructions for working with this code.

## Features Implemented

1. **Dictionary Creation for Documents**
   - Built a dictionary mapping `<DOCNO>` entries to unique numeric document IDs (1 to N).

2. **Content Selection**
   - Processed only the `<TITLE>` and `<TEXT>` sections of the documents for indexing.

3. **Text Normalization**
   - Case-normalized all documents.

4. **Tokenization**
   - Tokenized documents such that any sequence of alphanumeric characters and underscores (a-z, 0-9, _) forms a valid token.

5. **Token-to-ID Mapping**
   - Created a dictionary mapping tokens to unique numeric token IDs (1 to M).

6. **IDF Computation**
   - Computed the Inverse Document Frequency (IDF) for each token.

7. **TF-IDF Vector Construction**
   - Built cosine-normalized document vectors based on Term Frequency-Inverse Document Frequency (TF-IDF).

8. **Cosine Similarity Computation**
   - Computed pairwise cosine similarity for all document vectors.

9. **Similarity Ranking**
   - Sorted document pairs from most similar to least similar.
   - Extracted the top 50 most similar document pairs, outputting their `<DOCNO>` entries and similarity scores.

## Instructions

### Steps to Use the Code

1. **Input Preparation**
   - Ensure the input documents contain `<DOCNO>`, `<TITLE>`, and `<TEXT>` sections.

2. **Execution Workflow**
   - Run the code to:
     - Create document and token dictionaries.
     - Compute TF-IDF vectors.
     - Calculate pairwise cosine similarities.

3. **Output**
   - The code outputs the top 50 most similar document pairs with their similarity scores in the format:
     ```
     <DOCNO_1>, <DOCNO_2>, similarity_score
     ```

## Prerequisites

- Python 3.x
- Required Libraries:
  - `numpy`
  - `scipy`
  - `collections`

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Install necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the main script:
   ```bash
   python main.py
   ```

## Future Improvements

- Optimize tokenization for speed.
- Add support for stemming and stopword removal.
- Implement a graphical representation of similarity results.
- Enhance scalability for large datasets.

---

Contributions and feedback are welcome. Please feel free to raise issues or submit pull requests.
