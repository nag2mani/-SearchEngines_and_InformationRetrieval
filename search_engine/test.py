# This file is for testing purpose.

# Instruction
# You have to build tf x idf weighted vectors for every document and compute pairwise cosine similarity.


# Necessary steps:
# Build a dictionary of <DOCNO> entry to document-id (numeric: 1-N)
# Only use the <TITLE> and the <TEXT> Sections for indexing
# Case normalize the document
# Tokenize every document such that any sequence of alphanumeric characters and an underscore form a token (a-z, 0-9, _), each token is an index term
# Build a dictionary of token to token-id (numeric: 1-M)
# Compute token idfs.
# Build a tf x idf cosine normalized document vector.
# Compute pairwise document similarity.
# Sort document pairs from most similar to least similar, output <DOCNO> entry pairs and their similarity 




