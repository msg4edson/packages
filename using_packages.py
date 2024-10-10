# Define `random_words` and `random_word` but we're only importing one directly
from words import random_word

# Only* provides `randon_words` when the package is imported directly
from words import *

print(f"Random word generated: {random_word()}")
print(f"Random listed of word: {random_words(5)}")
