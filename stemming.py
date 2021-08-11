# Stemming
# https://realpython.com/nltk-nlp-python/#stemming

# Stemming is a text processing task in which you reduce words to their root, which is the core part of a word.
# For example, the words “helping” and “helper” share the root “help.”
# Stemming allows for zeroing in on the basic meaning of a word rather than all the details of how it’s being used.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

string_for_stemming = '''Here’s to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes. The ones who see 
things differently — they’re not fond of rules. You can quote them, disagree with them, glorify or vilify them, but the only thing you can’t do is 
ignore them because they change things. They push the human race forward, and while some may see them as the crazy ones, we see genius, 
because the ones who are crazy enough to think that they can change the world, are the ones who do. '''

words = word_tokenize(string_for_stemming)

print(words)
print('\n')

stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
