import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if response.status_code != 200:
            return None

        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".entry-preview .entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".nav-links .next::attr(href)").get()

    return next_page


# Requisito 4
def scrape_news(html_content):
    news_dict = {}
    selector = Selector(text=html_content)
    news_dict["url"] = selector.css(
        "head link[rel=canonical]::attr(href)"
    ).get()
    news_dict["title"] = (
        selector.css(".entry-title::text").get().strip(" \xa0")
    )
    news_dict["timestamp"] = selector.css(".meta-date::text").get()
    news_dict["writer"] = selector.css(".author a::text").get()
    news_dict["reading_time"] = int(
        selector.css(".meta-reading-time::text").re_first(r"\d+")
    )
    first_paragraph = selector.xpath("(//p)[1]//text()").getall()
    news_dict["summary"] = "".join(first_paragraph).strip(" \xa0")
    news_dict["category"] = selector.css(".meta-category .label::text").get()

    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
