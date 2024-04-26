"""
Author: Nagmani Kumar
Date: 25th April, 2023
Subject: SEIR
"""


# Creating a dictionary of filename as key and Natural number as value from 1 to N.
import os
folder_path = "./25"
files = os.listdir(folder_path)
documents_directory = {}
i=1
for file_name in files:
    documents_directory[file_name] = i
    i=i+1
# print("Documents_dictionary :", documents_directory)



# Text cleaning function.
def text_cleaner(text):
    chars_to_remove = ['.', ',', '(', ')', '[', ']', '{', '}', '@', "'", '&', '#', '^', '"', "-", "`", "!","/", "|",":",";"]
    for char in chars_to_remove:
        text = text.replace(char, " ")
    return text.split()



# Reading all the file content and making it dict_id to list of words.
docId_to_wordList_dict = {}
for file_name in documents_directory.keys():
    with open("./25/" + file_name, "r") as input_file:
        text = input_file.read()
        idx_title = text.find("<TITLE>")
        idx_end_title = text.find("</TITLE>")
        title_content = text[idx_title + 7 : idx_end_title]
        # print(title_content)
        cleaned_title_words = text_cleaner(title_content.lower())
        # print(cleaned_title_words)

        idx_text = text.find("<TEXT>")
        idx_end_text = text.find("</TEXT>")
        text_content =  text[idx_text + 7 : idx_end_text]
        # print(text_content)
        cleaned_text_words = text_cleaner(text_content.lower())
        # print(cleaned_text_words)

        doc_content = cleaned_title_words + cleaned_text_words
        docId_to_wordList_dict[documents_directory[file_name]] = doc_content
# print(docId_to_wordList_dict)



# Build a dictionary of token to token-id (numeric: 1-M)
unique_word_dict = {}
j=1
for key_id in docId_to_wordList_dict:
    for i in docId_to_wordList_dict[key_id]:
        if i not in unique_word_dict:
            unique_word_dict[i] = j
            j=j+1
# print(unique_word_dict)



# Calculating Document frequency of each words of dictonary.
unique_word_df_dict = {}
for i in unique_word_dict:
    cnt = 0
    for k in docId_to_wordList_dict:
        if i in docId_to_wordList_dict[k]:
            cnt = cnt + 1
    unique_word_df_dict[i] = cnt
# print("Document Frequency :", unique_word_df_dict)



# Calculating idef of each term.
import math
N=132
token_idf_dict={}
for one in unique_word_df_dict:
    token_idf_dict[one] = round(math.log2(N/unique_word_df_dict[one]), 2)
# print("Inverse Document Frequency :", token_idf_dict)



# Calculating Term frequency of words in a document.
from collections import Counter
doc_wise_tf = {}
j=1
for i in docId_to_wordList_dict:
    doc_dict = Counter(docId_to_wordList_dict[i])
    doc_wise_tf[j] = dict(doc_dict)
    j=j+1
# print("Document Term Frequency :", doc_wise_tf)



# Build a tf x idf cosine normalized document vector.
doc_wise_vectors = {}
m=1
for i in doc_wise_tf:
    temp_dict={}
    sum = 0
    for j in doc_wise_tf[i]:
        k = round(doc_wise_tf[i][j] * token_idf_dict[j], 2)
        sum = sum + k * k
    norm = math.sqrt(sum)

    for j in doc_wise_tf[i]:
        k = round(doc_wise_tf[i][j] * token_idf_dict[j], 2)
        temp_dict[j] = round(k/norm, 2)
    
    doc_wise_vectors[m] = temp_dict
    m=m+1
# print("doc_wise_Normalised_vectors :", doc_wise_vectors)




# Finding similarity between documents.
def find_similarity(d1, d2):
    # d1 and d2 are dictonary with key: term and value: normalised term.
    sum = 0
    for i in d1:
        if i in d2:
            sum = sum + d1[i] * d2[i]
        else:
            sum = sum
    return round(sum, 2)

doc_similarity_value = []

for i in range(1, 133):
    for j in range(i+1, 133):
        temp_similarity_val = [i,j]
        d1 = doc_wise_vectors[i]
        d2 = doc_wise_vectors[j]
        s = find_similarity(d1, d2)
        temp_similarity_val.append(s)
        doc_similarity_value.append(temp_similarity_val)



# Sorting documents on the basis of similarity score using lambda function.
sorted_data = sorted(doc_similarity_value, key=lambda x: x[2], reverse=True)



# Making top 50 documents with first_doc, 2nd_doc and similarity_score.
Top50_similar_documents = []
for i in sorted_data[:50]:
    temp=[]
    for j in documents_directory:
        if i[0] == documents_directory[j]:
            temp.append(j)
    for k in documents_directory:
        if i[1] == documents_directory[k]:
            temp.append(k)
    temp.append(i[2])
    Top50_similar_documents.append(temp)



# Printing Similarity score in Decreasing order for top 50 documents;
print("[First Documents, Second Documents, Similarity Score]")
for inner_list in Top50_similar_documents:
    print(inner_list)
    print()
