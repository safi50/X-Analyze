from flask import Flask, request, jsonify, render_template
from lda import SignIn, get_tweets,get_user_details, get_topics, gen_wordclouds
# from dotenv import load_dotenv

# load_dotenv() # Load environment variables
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', wordcloud_path=None)  # Pass None initially

@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']
    twitter_app = SignIn()  # Avoid using the same name 'app' as it shadows the Flask 'app'
    user = get_user_details(twitter_app, username)  # Retrieve user details

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
