# Tokenizing
# https://realpython.com/nltk-nlp-python/#tokenizing

# In Python tokenization basically refers to splitting up a larger body of text into smaller lines, words or even creating words for a non-English
# language.

# Tokenizing by word: allows for identifying of words that come up particularly often.
# Tokenizing by sentence: when you tokenize by sentence, you can analyze how those words relate to one another and see more context.

from nltk.tokenize import sent_tokenize, word_tokenize

example_string = '''Here’s to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes. The ones who see 
things differently — they’re not fond of rules. You can quote them, disagree with them, glorify or vilify them, but the only thing you can’t do is 
ignore them because they change things. They push the human race forward, and while some may see them as the crazy ones, we see genius, 
because the ones who are crazy enough to think that they can change the world, are the ones who do. '''

sentences = sent_tokenize(example_string)
for _ in sentences:
    print(_)

words = word_tokenize(example_string)
print(words)
