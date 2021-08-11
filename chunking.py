# Chunking
# https://realpython.com/nltk-nlp-python/#chunking

# While tokenizing allows you to identify words and sentences, chunking allows you to identify phrases.
# Chunking makes use of POS tags to group words and apply chunk tags to those groups.
# Chunks don’t overlap, so one instance of a word can be in only one chunk at a time.

import nltk
from nltk.tokenize import word_tokenize

# Before you chunking, the parts of speech in your text need to be tagged.
# Create a string for POS tagging:
lotr_quote = "It's a dangerous business, Frodo, going out your door."

words = word_tokenize(lotr_quote)
print(words)  # ['It', "'s", 'a', 'dangerous', 'business', ',', 'Frodo', ',', 'going', 'out', 'your', 'door', '.']

# Tag those words by part of speech:

# List of tuples of all the words in the quote, along with their POS tag.
pos_tags = nltk.pos_tag(words)
print(pos_tags)

# Create a chunk grammar with one regular expression rule.
# A chunk grammar consists of rules that indicate how sentences should be chunked.
# NP stands for noun phrase.
# More about noun phrase chunking: https://www.nltk.org/book/ch07.html#noun-phrase-chunking

# # This rule says that an NP chunk should be formed whenever the chunker finds an optional determiner (DT) followed by any number of
# adjectives (JJ) and then a noun (NN).

# The chunks:
# Start with an optional (?) determiner ('DT')
# Can have any number (*) of adjectives (JJ)
# End with a noun (<NN>)
grammar = 'NP: {<DT>?<JJ>*<NN>}'

# Create a chunk parser with this grammar:
chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(pos_tags)

# A visual representation of this tree:
tree.draw()
