drama_name = ['Outlander', 'Reign', 'Downton Abbey']
drama_url = ['https://en.wikipedia.org/wiki/Outlander_(TV_series)', 'https://en.wikipedia.org/wiki/Reign_(TV_series)', 'https://en.wikipedia.org/wiki/Downton_Abbey']
drama_negative = ['inaccurate', 'critics', 'ratings', 'mixed', 'cancellation', 'negative']
drama_positive = ['success', 'million', 'acclaimed', 'awards', 'nominations', 'positive' ]

# from GitHub and Stack Overflow
# imports

from mediawiki import MediaWiki

import bs4
import sys
import requests
import nltk
nltk.download()

def analyze_dramas():
    """ 
    For the historical dramas [Outlander, Reign, Downton Abbey], this function converts the pages to text files, performs a sentiment analysis checking for the presence of the listed positive and negative words and displaying their frequencies
    """
    for i in range(len(drama_name)):
        current = drama_name[i]
        wikipedia = MediaWiki()
        drama = wikipedia.page(current)
        print(drama.title)
        print(drama.content)
        url = drama_url[i]
        # implement this method to extract data from Wiki page and store as text file
        # from Stack Overflow 
        res = requests.get(url)
        res.raise_for_status()
        wiki = bs4.BeautifulSoup(res.text,"html.parser")
        file_to_write = open(url.split('/')[-1]+".txt", "a")
        for i in wiki.select('p'):
            text_to_write = i.getText().encode('utf-8') 
            file_to_write.write(str(text_to_write))

        file_to_write.close()
        from nltk.sentiment.vader import SentimentIntensityAnalyzer

        # use Professor's demo code in Notebook to begin sentiment analysis
        sentence = drama.content
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        print(score)
        
        f = open(f'{file_to_write.name}')  
        for line in f:
            # get rid of punctuation and spaces to not include in word count and create a variable of them
            # strippables = string.punctuation + string.whitespace (from analyze book demo code)
            word = (line.strip()).split()          
            punctuation_elements = ".,-_ "
            # create a dictionary to gauge frequency of positive and negative words
            wordfreq = {}
            for raw_word in word:
                word = raw_word.strip(punctuation_elements)
                if word not in wordfreq:
                    wordfreq[word] = 0 
                wordfreq[word] += 1
        for word in drama_negative:
            if word in wordfreq:
                print(word, wordfreq[word])
        for word in drama_positive:
            if word in wordfreq:
                print(word, wordfreq[word])
    
    
analyze_dramas()

