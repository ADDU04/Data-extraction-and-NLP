import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

# Load the Excel file
input_file = '20211030 Test Assignment\Input.xlsx'
df = pd.read_excel(input_file)


#Downloading stopwords and saving it.
nltk.download('stopwords')
nltk.download('punkt')
stop_words_folder = '20211030 Test Assignment\StopWords'
stop_words = set(stopwords.words('english'))

for filename in os.listdir(stop_words_folder):
    with open(os.path.join(stop_words_folder, filename), 'r') as file:
        for line in file:
            stop_words.add(line.strip().lower())

print(f"Loaded {len(stop_words)} stop words.")

def remove_stop_words(text):
    """
    Remove stop words from the input text using NLTK.

    Args:
    text (str): The input text to be processed.

    Returns:
    str: The text after removing stop words and non-alphanumeric characters.
    """
    words = word_tokenize(text)
    cleaned_text = ' '.join(word for word in words if word.lower() not in stop_words and word.isalnum())
    return cleaned_text

def creat_dict_pos_neg():
    """
    Create a dictionary of positive and negative words from predefined files.

    Returns:
    dict: A dictionary with keys 'positive' and 'negative', each containing a set of words.
    """
    master_dictionary_folder = '20211030 Test Assignment\MasterDictionary'

    # Initialize sets to hold positive and negative words
    positive_words = set()
    negative_words = set()

    # Load positive words
    with open(os.path.join(master_dictionary_folder, 'positive-words.txt'), 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word and word not in stop_words:  # Ensure the word is not a stop word
                positive_words.add(word)

    # Load negative words
    with open(os.path.join(master_dictionary_folder, 'negative-words.txt'), 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word and word not in stop_words:  # Ensure the word is not a stop word
                negative_words.add(word)

    print(f"Loaded {len(positive_words)} positive words.")
    print(f"Loaded {len(negative_words)} negative words.")

    # Create a dictionary with positive and negative words
    sentiment_dictionary = {
        'positive': set(positive_words),
        'negative': set(negative_words)
    }
    return sentiment_dictionary

def calculate_scores(text, pos_neg_words_dict):
    """
    Calculate sentiment scores for the input text.

    Args:
    text (str): The input text to be analyzed.
    dict1 (dict): A dictionary containing sets of positive and negative words.

    Returns:
    pd.Series: A Pandas Series containing positive score, negative score, polarity score, and subjectivity score.
    """
    words = word_tokenize(text.lower())
    total_words = len([word for word in words if word.isalnum()])

    positive_score = sum(1 for word in words if word in pos_neg_words_dict['positive'])
    #Note "we directly did sun of all negative words instead of assigning -1 value and then multiplying with -1 "
    negative_score = sum(1 for word in words if word in pos_neg_words_dict['negative'])

    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)

    return pd.Series([positive_score, negative_score, polarity_score, subjectivity_score])