import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt_tab')


def sentence_tokenization(paragraph):
    return sent_tokenize(paragraph)


paragraph = "This is a paragraph. It is for sentence tokenization. It is used in NLP to tokenize sentences."

tokenized_sentences = sentence_tokenization(paragraph)
for i in range(len(tokenized_sentences)):
    print(f"Sentence {i+1}: {tokenized_sentences[i]}")
