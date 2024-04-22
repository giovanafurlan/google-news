from GoogleNews import GoogleNews
import json

def get_news(query):
    googlenews = GoogleNews()
    googlenews.search(query)
    result = googlenews.result()
    return json.dumps(result)

if __name__ == "__main__":
    news = get_news("Python programming")
    print(news)
