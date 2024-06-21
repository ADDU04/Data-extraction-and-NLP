import requests
from bs4 import BeautifulSoup


def extract_and_return(df):
    """
    Extracts article text from URLs in a DataFrame and returns the DataFrame with the extracted text.

    This function iterates over a DataFrame containing URLs and attempts to fetch and extract the text of 
    articles from those URLs. The extracted text is then added to a new column in the DataFrame. If the 
    extraction fails for a particular URL, the corresponding row is excluded from the final DataFrame.

    Parameters:
    df (pd.DataFrame): A DataFrame containing at least two columns:
                       - 'URL_ID': A unique identifier for each URL.
                       - 'URL': The URL from which to extract article text.

    Returns:
    pd.DataFrame: The original DataFrame with an additional column 'Article_Text' containing the extracted 
                  article text. Rows for which the article text could not be extracted are removed.
    """
    
    def extract_article_text(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # find article title and text, to be customized per site structure
                title = soup.find('h1').get_text(strip=True)
                paragraphs = soup.find_all('p')
                article_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])
                
                return title + '\n' + article_text
            else:
                return None
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    # Create a new column for the article text
    df['Article_Text'] = ''

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        
        print(f"Processing URL_ID: {url_id} - URL: {url}")
        
        article_content = extract_article_text(url)
        if (article_content):
            df.at[index, 'Article_Text'] = article_content
            print(f"Extracted article for URL_ID: {url_id} successfully.")
        else:
            df.at[index, 'Article_Text'] = None
            print(f"Failed to extract article for URL_ID: {url_id}")

    df = df.dropna()
    return df