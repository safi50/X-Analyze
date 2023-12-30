import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from tweety import Twitter
from tweety.exceptions_ import UserNotFound
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from wordcloud import WordCloud


# Ensure NLTK data is downloaded
# nltk.download('stopwords')
# nltk.download('wordnet')

def SignIn():
    app = Twitter("session")
    app.sign_in("x_analyze", "YY3nSOYJIzVRZy9A5b5o")
    return app

# load_dotenv() # Load environment variables

# def SignIn():
#     twitter_username = os.environ.get('TWITTER_USERNAME')
#     twitter_password = os.environ.get('TWITTER_PASSWORD')
#     print(twitter_username, twitter_password)
#     if not twitter_username or not twitter_password:
#         raise ValueError("Twitter credentials are not set in the environment variables.")
#     app = Twitter("session")
#     app.sign_in(twitter_username, twitter_password)
#     return app

    
def get_tweets(app, username):
    try: 
        all_tweets = app.get_tweets(username)
        tweets = []
        for tweet in all_tweets:
            if hasattr(tweet, 'tweet_body') and tweet.tweet_body:
                tweets.append(tweet.tweet_body)
        return tweets
    except UserNotFound:
        return None


def get_user_details(app, username):
    try:
        user = app.get_user_info(username)
        return user
    except UserNotFound:
        return None


def processTweet(tweet):
    tokenizer = RegexpTokenizer(r'\w+')
    en_stopwords = set(stopwords.words('english'))
    en_stopwords.update(['rt', 'via'])  
    tweet = tweet.lower()

    # Removing URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    # Removing user @ mentions and hashtags
    tweet = re.sub(r'@\w+|#\w+', '', tweet)
    # Removing non-ASCII characters
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    # Tokenizing the tweet
    tokens = tokenizer.tokenize(tweet)
    # Removing stopwords and short words
    new_tokens = [token for token in tokens if token not in en_stopwords and len(token) > 2]
    return new_tokens


def get_topics(tweets, num_topics=2):
    processed_tweets = [processTweet(tweet) for tweet in tweets]
    dictionary = corpora.Dictionary(processed_tweets)
    doc_term_matrix = [dictionary.doc2bow(tweet) for tweet in processed_tweets]
    lda_model = LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=100)
    return lda_model

def gen_wordclouds(lda_model, num_topics):
    for t in range(num_topics):
        topic_terms = dict(lda_model.show_topic(t, 180))
        wordcloud = WordCloud(width=1200, height=500, background_color='white')
        wordcloud.generate_from_frequencies(topic_terms)
        wordcloud.to_file(f'static/wordcloud_topic_{t+1}.png')  

