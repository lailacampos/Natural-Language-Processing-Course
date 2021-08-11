# Lemmatizing
# https://realpython.com/nltk-nlp-python/#lemmatizing

# Lemmatizing reduces words to their core meaning, but it will give you a complete English word that makes sense on its own instead of just a
# fragment of a word.

# Note: A lemma is a word that represents a whole group of words, and that group of words is called a lexeme.

# "blending":
# "blend” is the lemma.
# "blending" is the lexeme.

# When you lemmatize a word, you are reducing it to its lemma.

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('scarves'))  # scarf

# Create a string with more than one word to lemmatize:
string_for_lemmatizing = 'The friends of DeSoto love scarves.'

# Tokenize that string by word:
words = word_tokenize(string_for_lemmatizing)
print(words)  # ['The', 'friends', 'of', 'DeSoto', 'love', 'scarves', '.']

# Create a list containing all the words in words after they’ve been lemmatized:
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)  # ['The', 'friend', 'of', 'DeSoto', 'love', 'scarf', '.']

######################################################################################

# Lemmatizing a word that looked very different from its lemma:
print(lemmatizer.lemmatize('worst'))  # worst

# The result is 'worst' because lemmatizer.lemmatize() assumed that "worst" was a noun.
# It's possible to make clear that you want "worst" to be an adjective:
print(lemmatizer.lemmatize('worst', pos='a'))  # bad

# "worst" is the superlative form of the adjective 'bad', and lemmatizing reduces superlatives as well as comparatives to their lemmas.
