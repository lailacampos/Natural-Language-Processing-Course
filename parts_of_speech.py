# Tagging Parts of Speech
# https://realpython.com/nltk-nlp-python/#tagging-parts-of-speech

# Part of speech is a grammatical term that deals with the roles words play when you use them together in sentences.
# Tagging parts of speech, or POS tagging, is the task of labeling the words in your text according to their part of speech.
import nltk
from nltk.tokenize import word_tokenize

example_string = "If you wish to make an apple pie from scratch, you must first invent the universe."

# Use word_tokenize to separate the words in that string and store them in a list:
words = word_tokenize(example_string)
print(words)

# Call nltk.pos_tag() on new list of words
pos_word_list = nltk.pos_tag(words)

# All the words in the quote are now in a separate tuple, with a tag that represents their part of speech.
print(pos_word_list)

