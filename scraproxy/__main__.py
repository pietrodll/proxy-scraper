"""Main module"""

from .scrapers import FreeProxyList

if __name__ == "__main__":
    FPL = FreeProxyList()

    FILTER_FUNC = lambda proxy: proxy.last_checked <= 60

    FPL.to_json(filter_func=FILTER_FUNC)
