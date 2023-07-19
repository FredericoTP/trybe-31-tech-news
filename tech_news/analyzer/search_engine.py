from tech_news.database import db
from datetime import datetime

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
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")

        date_news = db.news.find(
            {"timestamp": datetime.strftime(date_format, "%d/%m/%Y")},
            {"title": True, "url": True},
        )

        news_to_return = []
        for n in date_news:
            news_to_return.append((n["title"], n["url"]))

        return news_to_return
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    category_news = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": True, "url": True},
    )

    news_to_return = []
    for n in category_news:
        news_to_return.append((n["title"], n["url"]))

    return news_to_return
