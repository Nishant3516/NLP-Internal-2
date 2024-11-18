import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')


def stemming(paragraph):
    stemmer = PorterStemmer()
    words = word_tokenize(paragraph)
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)


paragraph = "This is a paragraph. It is for stemming. It is used in NLP to stem words by removing prefixes and suffixes."
stemmed_words = stemming(paragraph)
print(stemmed_words)
