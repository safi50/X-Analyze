from flask import Flask, request, jsonify, render_template
from lda import SignIn, get_tweets,get_user_details, get_topics, gen_wordclouds

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', wordcloud_path=None)  

@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']
    twitter_app = SignIn() 
    user = get_user_details(twitter_app, username) 

    if user is None:
        error_message = "The User Account wasn't Found"
        return render_template('index.html', error_message=error_message)

    tweets = get_tweets(twitter_app, username)
    lda_model = get_topics(tweets, 1)
    gen_wordclouds(lda_model, 1)
    
    wordcloud_path = 'static/wordcloud_topic_1.png'
    return render_template('index.html', wordcloud_path=wordcloud_path, user_details=user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
