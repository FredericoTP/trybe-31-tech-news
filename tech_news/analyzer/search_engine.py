from tech_news.database import db


# Operador $regex:
# https://www.mongodb.com/docs/v6.0/reference/operator/query/regex/


# Requisito 7
def search_by_title(title):
    title_news = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": True, "url": True},
    )

    news_to_return = []
    for n in title_news:
        news_to_return.append((n["title"], n["url"]))

    return news_to_return


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
