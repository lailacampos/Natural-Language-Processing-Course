# Frequency Distribution
# https://realpython.com/nltk-nlp-python/#making-a-frequency-distribution

# With a frequency distribution, it's possible to check which words show up most frequently in a text.

from nltk import FreqDist
from nltk.book import *
from nltk.corpus import stopwords

frequency_distribution = FreqDist(text8)
print(frequency_distribution)  # <FreqDist with 1108 samples and 4867 outcomes>

# 20 most common words in the corpus:
# .most_common() returns a list containing tuples that have two elements each: the word and the number of times it appears.
# for i in frequency_distribution.most_common(20):
    # print(i)
# print(frequency_distribution.most_common(20))

# Removing stop words.

stop_words = set(stopwords.words('english'))

# Create a list of all of the words in text8 that aren’t stop words:
meaningful_words = [word for word in text8 if word.casefold() not in stop_words]

# Make a frequency distribution:
frequency_distribution = FreqDist(meaningful_words)

for i in frequency_distribution.most_common(20):
    print(i)

# Plotting a graph with the most common meaningful words:
frequency_distribution.plot(20, cumulative=True)
