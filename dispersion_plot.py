# Making a Dispersion Plot
# https://realpython.com/nltk-nlp-python/#making-a-dispersion-plot

# It's possible to use a dispersion plot to see how much a particular word appears and where it appears.

from nltk.book import *

text8.dispersion_plot(['woman', 'lady', 'girl', 'gal', 'man', 'gentleman', 'boy', 'guy'])

# Each vertical blue line represents one instance of a word.
# Each horizontal row of blue lines represents the corpus as a whole.

# Use a dispersion plot when you want to see where words show up in a text or corpus.
# On the analysis of a single text, this can help to see which words show up near each other.
# On the analysis of a corpus of texts that is organized chronologically, it can help to see which words were being used more or less over a period
# of time.
