from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter
import praw
import json
import pprint
from config import client_id, client_secret, username, password, user_agent

reddit = praw.Reddit(client_id= client_id,
                     client_secret= client_secret,
                     username= username,
                     password= password,
                     user_agent= user_agent)
                     
def find_top_x_on_subreddit(x, time, subreddit):
    """
    This is a function that returns the Top Posts on a Sub reddit given the following:
    x = number of posts 
    time = top of what category i.e. 'day', 'week', 'month' (string)
    subreddit = a subreddit you like i.e.'NatureIsFuckingLit' (string)
    """
    sub = subreddit
    submissions = reddit.subreddit(sub).top(time, limit= x)
    top = [(submission.title, submission.selftext) for submission in submissions]
    return top

# print(find_top_x_on_subreddit(10,'day', 'NatureIsFuckingLit'))


# sub = 'NatureIsFuckingLit'
# submissions = reddit.subreddit(sub).top('day', limit=10)
# top10 = [(submission.title, submission.selftext) for submission in submissions]
# pprint.pprint(top10)


# I am doing this to sort through the unneeded empty space in the data
def return_list_of_headlines(top):
    """
    This function returns a list out of the first item in a tupple
    This function is being used to clean up Reddit Post Titles
    
    To find Top on subreddit:
    sub = A string of the SubReddit
    submissions = reddit.subreddit(sub).top('day', limit= "a numerical value")
    top = [(submission.title, submission.selftext) for submission in submissions]
    """
    l = []
    for headline in top:
        only_headline = headline[0]
        l.append(only_headline)
        # print(only_headline)
    # print(l)
    return l


def list_item_counter(l):
    """
    This is a function that counts items in a list
    """
    d = dict()
    for c in l:
        for letter in c:
            # print(word)
            if letter not in d:
            # d[c] This is a key in value 
                d[letter] = 1
            else: 
                d[letter] += 1
    return d
    

# print(list_item_counter(return_list_of_headlines(find_top_x_on_subreddit(10, 'day', 'NatureIsFuckingLit'))))


topx = find_top_x_on_subreddit(10,'day', 'NatureIsFuckingLit')
list_of_headlines = return_list_of_headlines(topx)
def find_headline_sentiment(list_of_headlines):
    """
    This function prints each given headline along with its sentiment score:
    list_of_headlines = (list)
    """
    for headline in list_of_headlines:
        sentence = headline
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        print(headline, score)

# # print(str_content)
# sentence = str_content
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# # print(score)



if __name__ == '__main__':
    topx = find_top_x_on_subreddit(10,'day', 'NatureIsFuckingLit')
    list_of_headlines = return_list_of_headlines(topx)
    # print(f'This is a list of the top headlines on r/NatureIsFuckingLit: {list_of_headlines}')
    find_headline_sentiment(list_of_headlines)
