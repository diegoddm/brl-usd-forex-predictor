import feedparser

def get_news():
    feed = feedparser.parse("https://news.google.com/rss/search?q=dólar+OR+brasil+economia+OR+usd+brl&hl=pt-BR&gl=BR&ceid=BR:pt-419")
    news = []
    for entry in feed.entries[:10]:
        news.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return news
