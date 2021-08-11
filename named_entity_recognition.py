# Named Entity Recognition
# https://realpython.com/nltk-nlp-python/#using-named-entity-recognition-ner

# Named entities are noun phrases that refer to specific locations, people, organizations, and so on.
# With named entity recognition, it's possible to find the named entities in texts and also determine what kind of named entity they are.

import nltk
from nltk.tokenize import word_tokenize

lotr_quote = "It's a dangerous business, Frodo, going out your door."

words = word_tokenize(lotr_quote)
print(words)  # ['It', "'s", 'a', 'dangerous', 'business', ',', 'Frodo', ',', 'going', 'out', 'your', 'door', '.']

# List of tuples of all the words in the quote, along with their POS tag.
pos_tags = nltk.pos_tag(words)
print(pos_tags)

# Visual representation:
tree = nltk.ne_chunk(pos_tags)
# tree.draw()

######################################################################################

# Extracting named entities directly from text.

quote = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.
During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2."""


# Function to extract named entities:
# Gather all named entities, with no repeats.
def extract_named_entity(quote):

    # Tokenize by word
    words = word_tokenize(quote)

    # Apply part of speech tags to those words:
    tags = nltk.pos_tag(words)

    # Because binary=True, the named entities you’ll won’t be labeled more specifically. You’ll just know that they’re named entities.
    tree = nltk.ne_chunk(tags, binary=True)

    # Extract named entities based on those tags.
    return set(

        # Takes the first element of the tuple (the word itself) and join the string ' '.
        ' '.join(i[0] for i in t)

        # For each element in tree of chunks
        for t in tree

        # The hasattr() method returns true if an object has the given named attribute and false if it does not.
        # hasattr(object, name)
        if hasattr(t, 'label') and t.label() == 'NE'
    )

print(extract_named_entity(quote))  # {'Perrotin', 'Mars', 'Nature', 'Schiaparelli', 'Lick Observatory'}