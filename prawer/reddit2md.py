import praw, requests, datetime, re
import settings
from urllib.parse import urlparse

def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    try:
        if r.headers["content-type"] in image_formats:
            return True
    except:
        return False

def is_url(url):
    try:
      result = urlparse(url)
      return all([result.scheme, result.netloc])
    except ValueError:
      return False
        

def get_date_post(submission):
	time = submission.created_utc
	return datetime.datetime.fromtimestamp(time)

def reddit2md(praw, link, file_name = None):
    if link.startswith('"') and link.endswith('"'):
        link = link.rstrip('"').lstrip('"')
    
    thepost = praw.submission(url=link)

    if not thepost.is_self:
        raise Exception("Only text posts are supported.")

    md_splitted = thepost.selftext.splitlines()
    result_md = []

    for line in md_splitted:
        if is_url(line):
            if is_url_image(line):
                line = '![]({url})'.format(url = line)
        result_md.append(line)

    result = {
        "title": thepost.title,
        "selftext": result_md,
        "author": thepost.author.name,
        "url": link,
        "created_date": get_date_post(thepost),
        "subreddit": thepost.subreddit.display_name
    }

    return result
        
