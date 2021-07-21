import settings
from flask import Flask, request, abort, Response, render_template
from prawer.reddit2md import reddit2md
import praw
import time

app = Flask(__name__)

reddit = praw.Reddit(
                client_id = settings.credentials['client_id'],
                client_secret = settings.credentials['client_secret'],
                user_agent = settings.credentials['user_agent'],
            )


@app.route("/", methods = ['GET', 'POST'])
def r2m():
    if request.method == 'POST':
        start = time.time()
        data = request.form
        if len(data) == 0:
            return render_template('error.html')
        if data["url"] is None:
            return render_template('error.html')

        try:
            reddit_url = data["url"]
            md_result = reddit2md(reddit, reddit_url)

            result = {
                'title': md_result['title'],
                'selftext': md_result['selftext'],
                'author': md_result['author'],
                'author_url': "https://reddit.com/u/" + md_result['author'],
                'post_url': md_result['url'],
                'created_date': md_result['created_date'],
                'subreddit': md_result['subreddit'],
                'subreddit_url': "https://reddit.com/r/" + md_result['subreddit']
            }

            return render_template('r2m.html', **result)
        except:
            return render_template('error.html')

    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)