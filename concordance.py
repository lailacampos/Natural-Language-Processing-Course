# Concordance

# Getting Text to Analyze:
# A group of texts is called a corpus. NLTK provides several corpora.
# In order to analyze texts in NLTK, they need to be imported.

from nltk.book import *

# Using a Concordance

# When you use a concordance, you can see each time a word is used, along with its immediate context.
# This allows for a peek into how a word is being used at the sentence level and what words are used with it.

print(text8.concordance('man'))
print(text8.concordance('woman'))
