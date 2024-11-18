import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')


def word_tokenization(paragraph):
    return word_tokenize(paragraph)


paragraph = "This is a paragraph. It is for word tokenization. It is used in NLP to tokenize sentences into words."

tokenized_words = word_tokenization(paragraph)
print(tokenized_words)
