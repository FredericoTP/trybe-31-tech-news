from tech_news.database import db


# Requisito 10
def top_5_categories():
    categories = db.news.find({}, {"category": True})

    all_categories = {}

    for category in categories:
        if all_categories.get(category["category"]):
            all_categories[category["category"]] += 1
        else:
            all_categories[category["category"]] = 1

    sorted_categories = list(
        dict(
            sorted(
                all_categories.items(), key=lambda item: (-item[1], item[0])
            )
        ).keys()
    )

    return sorted_categories[:5]
