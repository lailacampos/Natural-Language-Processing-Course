# Chinking
# https://realpython.com/nltk-nlp-python/#chinking

# While chunking is used to include a pattern, chinking is used to exclude a pattern.

import nltk
from nltk.tokenize import word_tokenize

lotr_quote = "It's a dangerous business, Frodo, going out your door."

words = word_tokenize(lotr_quote)
print(words)  # ['It', "'s", 'a', 'dangerous', 'business', ',', 'Frodo', ',', 'going', 'out', 'your', 'door', '.']

# List of tuples of all the words in the quote, along with their POS tag.
pos_tags = nltk.pos_tag(words)
print(pos_tags)

# Create a grammar to determine what to include and exclude in the chunks.

# The first rule of your grammar is {<.*>+}
# This rule has curly braces that face inward ({}) because it’s used to determine what patterns to include in the chunks.
# In this case, include everything: <.*>+.

# The second rule of your grammar is }<JJ>{
# This rule has curly braces that face outward (}{) because it’s used to determine what patterns you want to exclude in the chunks.
# In this case, exclude adjectives: <JJ>.
grammar = '''
Chunk: {<.*>+}
}<JJ>{'''

# Create a chunk parser with this grammar:
chunk_parser = nltk.RegexpParser(grammar)
print(chunk_parser)

# Chunk the sentence with the chink specified:
tree = chunk_parser.parse(pos_tags)

tree.draw()
