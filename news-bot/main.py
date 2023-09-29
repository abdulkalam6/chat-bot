import requests
import json
import nltk
from newspaper import Article

def fetch_article_url(api_key):
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        articles = data.get("articles", [])
        if articles:
            return articles[0]["url"]
        else:
            return None
    else:
        print("Failed to fetch the news article")
        return None

def download_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article

def save_article_text_and_summary(article):
    with open('article.txt', 'w', encoding='utf-8') as f:
        f.write(article.text)

    article.nlp()
    with open('summary.txt', 'w', encoding='utf-8') as f:
        f.write(article.summary)

def main():
    api_key = "a83df0e6056b4cef8d48bd7b998507dd"
    
    nltk.download('punkt')  
    
    article_url = fetch_article_url(api_key)
    if article_url:
        article = download_article(article_url)
        print(f"Article URL: {article_url}")
        save_article_text_and_summary(article)

if __name__ == "__main__":
    main()
