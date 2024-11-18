import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")

stopwords_eng = set(stopwords.words('english'))

paragraph = "This is a paragraph. It is for word tokenization. It is used in NLP to tokenize sentences into words."

words = word_tokenize(paragraph)

filtered_words = [i for i in words if i not in stopwords_eng]

print(filtered_words)
