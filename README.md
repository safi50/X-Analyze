# X-Analyze


X-Analyze is a Flask-based web application designed to analyze Twitter user profiles. Utilizing natural language processing techniques, it provides insights into the topics expressed in a user's tweets. With a focus on user experience, X-Analyze offers an intuitive and visually engaging interface for understanding the social media footprint of any public Twitter account.

## Features
- **User Profile Analysis:** Enter a Twitter username to retrieve a comprehensive analysis of the user's recent tweets.
- **Topic Modeling:** Discover the most prominent topics discussed by a user, using LDA (Latent Dirichlet Allocation) for topic extraction.
- **Word Cloud Visualization:** Visualize the most frequent words used by the user in a dynamic word cloud.
- **Responsive Design:** Enjoy a seamless experience across various devices and screen sizes.

## Technologies Used
- **Backend:** Flask (Python) , Docker
- **Frontend:** HTML, CSS, JavaScript
- **NLP Library:** NLTK, Gensim, WordCloud
- **API:** Custom Twitter API integration
- **Deployment:** Koyeb

## Steps to Run
1. Clone Github Repository : `git clone  https://github.com/safi50/XAnalyze.git`
2. Install Dependencies : `pip install -r requirements.txt`
3. To Run Locally : `python app.py`
4. To Build and Run on Docker :
       ```
   docker build -t xanalyze .
   docker run -p 8000:8000 xanalyze     
   ```

## Author
- Syed Safi Ullah Shah - github.com/safi50
