import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('wordnet')

paragraph = "This is a paragraph. It is for Lemmatization. Unlike stemming, which simply removes prefixes or suffixes, lemmatization uses a vocabulary and morphological analysis to return the correct base form."


words = word_tokenize(paragraph)

lemmatizer = WordNetLemmatizer()
lemmatizedWords = [lemmatizer.lemmatize(word) for word in words]
print(" ".join(lemmatizedWords))
