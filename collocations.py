# Finding Collocations
# https://realpython.com/nltk-nlp-python/#finding-collocations

# A collocation is a sequence of words that shows up often.
import nltk
from nltk.book import *
from nltk.stem import WordNetLemmatizer

# To see pairs of words that come up often in a corpus, call .collocations() on it:
print()
print(text8.collocations())

######################################################################################

# Looking for collocations after lemmatizing the words:

# Create an instance of WordNetLemmatizer:
lemmatizer = WordNetLemmatizer()

# Create a list of the lemmatized versions of all the words in text8:
lemmatized_words = [lemmatizer.lemmatize(word) for word in text8]

# In order to be able to do the linguistic processing tasks seen so far, a NLTK text needs to be made with this list:
# https://www.nltk.org/api/nltk.html#nltk.text.Text
# A NLTK text is a wrapper around a sequence of simple (string) tokens, which is intended to support initial exploration of texts
# (via the interactive console).
new_text = nltk.Text(lemmatized_words)

# See the collocations in new_text:
print()
print(new_text.collocations())
