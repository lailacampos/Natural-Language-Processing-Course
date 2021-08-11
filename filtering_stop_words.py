# Filtering Stop Words
# https://realpython.com/nltk-nlp-python/#filtering-stop-words

# Stop words are words that you want to ignore, so you filter them out of your text when you’re processing it.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "Here's to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes."
words = word_tokenize(example_sentence)
print(words)

# The next step is to create a set of stop words to filter example_sentences
stop_words = set(stopwords.words('english'))

# Create an empty list to hold the words that make it past the filter. All the words in 'words' that aren't stop words.
filtered_list = []

# Iterates over 'words' with a for loop and adds all the words that aren't stop words to filtered_list.
for word in words:
    # Use .casefold() on 'word' to ignore whether the letters in word are uppercase or lowercase.
    # This is worth doing because stopwords.words('english') includes only lowercase versions of stop words.
    if word.casefold() not in stop_words:
        filtered_list.append(word)

print(filtered_list)

# Alternatively, using list comprehensions:
# https://realpython.com/list-comprehension-python/#using-list-comprehensions
# new_list = [expression for member in iterable]
# Example of list comprehension:
# squares = [i * i for i in range(10)]
filtered_list2 = [word for word in words if word.casefold() not in stop_words]
print(filtered_list2)

print(filtered_list == filtered_list2)  # Both filtered lists have the same elements so it evaluates to True
