import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
import re

# Function to do Analysis of Readablity
def find_complex_words(words):
    """
    Count the number of complex words (words with three or more syllables) in a list of words.

    Args:
    words (list): A list of words to be analyzed.

    Returns:
    int: The number of complex words in the list.
    """
    return sum(1 for word in words if count_syllables(word) >= 3)

def calculate_readability(text):
    """
    Calculate readability metrics for the input text.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    pd.Series: A Pandas Series containing average sentence length, percentage of complex words, and fog index.
    """
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_words = len([word for word in words if word.isalnum()])
    num_sentences = len(sentences)
    num_complex_words = find_complex_words(words)

    if num_sentences == 0:  # Avoid division by zero
        average_sentence_length = 0
    else:
        average_sentence_length = num_words / num_sentences

    if num_words == 0:  # Avoid division by zero
        percentage_complex_words = 0
    else:
        percentage_complex_words = num_complex_words / num_words

    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    return pd.Series([average_sentence_length, percentage_complex_words, fog_index])

# Function to count complex words
def count_complex_words(text):
    """
    Count the number of complex words (words with more than two syllables) in the input text.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    int: The number of complex words in the text.
    """
    words = word_tokenize(text.lower())
    complex_words = [word for word in words if count_syllables(word) > 2]
    return len(complex_words)



# Function to Calculate Word Count(cleaned words count)
def count_cleaned_words(text):
    """
    Count the number of cleaned words (excluding stopwords and punctuation) in the input text.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    int: The number of cleaned words in the text.
    """
    words = word_tokenize(text.lower())
    cleaned_words = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    return len(cleaned_words)

# Function to count Syllable Per Word
def count_syllables(word):
    """
    Count the number of syllables in a word.

    Args:
    word (str): The word to be analyzed.

    Returns:
    int: The number of syllables in the word.
    """
    vowels = 'aeiouy'
    word = word.lower().strip(string.punctuation)

    if not word:
        return 0

    count = 0
    prev_char_vowel = False

    for char in word:
        if char in vowels:
            if not prev_char_vowel:  # New syllable found
                count += 1
            prev_char_vowel = True
        else:
            prev_char_vowel = False

    # Handle exceptions for endings 'es' and 'ed'
    if word.endswith('es') or word.endswith('ed'):
        count -= 1

    # Ensure at least one syllable counted for very short words
    if count == 0:
        count = 1
    return count


# Function to count Personal Pronouns
def count_personal_pronouns(text):
    """
    Count the number of personal pronouns in the input text.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    int: The number of personal pronouns in the text.
    """
    personal_pronouns = re.findall(r'\b(?:I|we|my|ours|us)\b', text.lower())
    # Exclude 'us' when it's part of a country name like 'United States'
    personal_pronouns = [word for word in personal_pronouns if word != 'us']
    return len(personal_pronouns)


# Function to count Average Word Length
def calculate_average_word_length(text):
    """
    Calculate the average word length in the input text.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    float: The average word length in the text.
    """
    words = word_tokenize(text.lower())
    total_characters = sum(len(word) for word in words if word.isalnum())
    total_words = len(words)
    average_word_length = total_characters / total_words if total_words > 0 else 0
    return average_word_length

# post processing for column  renaming
def rename_columns(df):
    # Define a dictionary for the new column names
    new_column_names = {
        'Positive_Score': 'POSITIVE SCORE',
        'Negative_Score': 'NEGATIVE SCORE',
        'Polarity_Score': 'POLARITY SCORE',
        'Subjectivity_Score': 'SUBJECTIVITY SCORE',
        'Average_Sentence_Length': 'AVG SENTENCE LENGTH',
        'Percentage_Complex_Words': 'PERCENTAGE OF COMPLEX WORDS',
        'Fog_Index': 'FOG INDEX',
        'Average_Words_Per_Sentence': 'AVG NUMBER OF WORDS PER SENTENCE',
        'Complex_Word_Count': 'COMPLEX WORD COUNT',
        'Word_Count': 'WORD COUNT',
        'Syllable_Count': 'SYLLABLE PER WORD',
        'Personal_Pronoun_Count': 'PERSONAL PRONOUNS',
        'Average_Word_Length': 'AVG WORD LENGTH'
    }
    
    # Rename the columns
    df.rename(columns=new_column_names, inplace=True)
    
    return df