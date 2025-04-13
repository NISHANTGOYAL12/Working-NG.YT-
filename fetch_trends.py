from pytrends.request import TrendReq

def get_trending_topics(keyword="Indian Mythology"):
    pytrends = TrendReq()
    pytrends.build_payload([keyword], cat=0, timeframe='now 1-d', geo='IN', gprop='youtube')
    return pytrends.related_queries()[keyword]['top']
