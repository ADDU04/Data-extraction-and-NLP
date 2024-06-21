from Sentiments_Analysis import *
from Other_analysis import *
from DataExtraction import *
df=pd.read_excel('20211030 Test Assignment\Input.xlsx')
df = extract_and_return(df)

#1.1 Cleaning using Stop Words Lists
df['Cleaned_Article_Text'] = df['Article_Text'].apply(remove_stop_words)
#1.2 Creating dictionary of Positive and Negative words
dict_pos_neg = creat_dict_pos_neg()
#1.3	Extracting Derived variables
df[['Positive_Score', 'Negative_Score', 'Polarity_Score', 'Subjectivity_Score']] = df['Cleaned_Article_Text'].apply(lambda text: calculate_scores(text, dict_pos_neg))

#2 Analysis of Readability
df[['Average_Sentence_Length', 'Percentage_Complex_Words', 'Fog_Index']] = df['Article_Text'].apply(calculate_readability)

#3	Average Number of Words Per Sentence
#4	Complex Word Count	3
#5	Word Count
#6  Syllable Count Per Word
df[['Average_Words_Per_Sentence', 'Word_Count', 'Complex_Word_Count', 'Syllable_Count']] = df['Article_Text'].apply(lambda text: pd.Series([
    len(word_tokenize(text)) / len(sent_tokenize(text)) if len(sent_tokenize(text)) > 0 else 0,  # Average Words per Sentence
    count_cleaned_words(text),  # Word Count
    count_complex_words(text),  # Complex Word Count
    sum(count_syllables(word) for word in word_tokenize(text))  # Syllable Count
]))

#7	Personal Pronouns
df['Personal_Pronoun_Count'] = df['Article_Text'].apply(lambda text: count_personal_pronouns(text))

#8	Average Word Length
df['Average_Word_Length'] = df['Article_Text'].apply(lambda text: calculate_average_word_length(text))
print(df)
 
 #post processing
df=rename_columns(df)

(df.to_excel('Output.xlsx',sheet_name= "Data Extraction and NLP"))