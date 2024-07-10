## Sentiment Analysis

# Cleaning using Stop Words Lists
Stop words from the StopWords folder are removed to clean the text for sentiment analysis.

# Creating a dictionary of Positive and Negative words
Using the MasterDictionary (from MasterDictionary folder), we compile lists of positive and negative words, excluding stop words.

### Extracting Derived Variables
Using NLTK tokenize module, the following variables are calculated:
- Positive Score: Sum of positive word occurrences.
- Negative Score: Sum of negative word occurrences (multiplied by -1).
- Polarity Score: Sentiment score ranging from -1 (negative) to +1 (positive).
- Subjectivity Score: Score determining objectivity or subjectivity ranging from 0 (objective) to +1 (subjective).

## Analysis of Readability

# Average Number of Words Per Sentence
Calculated by dividing the total number of words by the total number of sentences.

# Complex Word Count
Identifying words with more than two syllables to gauge complexity.

# Word Count
Total number of cleaned words in the text, excluding stop words and punctuation.

# Syllable Count Per Word
Counting syllables per word, handling exceptions like words ending with "es" or "ed".

# Personal Pronouns
Using regex, counts of personal pronouns like "I," "we," "my," "ours," and "us" are calculated, excluding the country name "US".

# Average Word Length
Average length of words calculated by dividing the total number of characters by the total number of words.


# Gunning Fox Index (Readability Metric)
- Average Sentence Length: Number of words divided by the number of sentences.
- Percentage of Complex Words: Ratio of complex words to total words.
- Fog Index: Calculated as 0.4 * (Average Sentence Length + Percentage of Complex Words).



##How to run 

Step 1 
Pip install -r requirements.txt
Step 2 
Run main.py file