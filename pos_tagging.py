import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

paragraph = "This is a paragraph. It is for POS tagging. It is used in NLP for tagging the words with respective POS."

words = word_tokenize(paragraph)

tagged = pos_tag(words)

print(tagged)
