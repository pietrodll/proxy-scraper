"""Main module"""

from .scrapers import FreeProxyLists

if __name__ == "__main__":
    FPL = FreeProxyLists()

    print(FPL.proxies)

    # FILTER_FUNC = lambda proxy: proxy.last_checked <= 60

    # FPL.to_json(filter_func=FILTER_FUNC)
