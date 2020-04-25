"""This module contains the `ProxyScraper` class"""

from abc import ABCMeta, abstractmethod
import json
import requests as r
from bs4 import BeautifulSoup


class ProxyScraper(metaclass=ABCMeta):
    """Absctract class to scrape proxy websites. It has to be overridden for every proxy website"""

    website_url = None

    def __init__(self, load_later=False):
        self._proxies = []

        if not load_later:
            self.load_proxies()

    @abstractmethod
    def load_proxies(self):
        """Loads the proxy list from the website"""

    @property
    def proxies(self):
        """Returns the proxy list"""

        return self._proxies[:]

    def _get_soup(self):
        """Gets the BeautifulSoup object of the website"""

        site = r.get(self.website_url).text
        return BeautifulSoup(site, features='html.parser')

    def to_json(self, filename='proxies.json', filter_func=None):
        """Saves the proxies as a JSON file"""

        proxies = self._proxies
        if filter_func is not None:
            proxies = filter(filter_func, proxies)

        proxy_json = [proxy.to_dict() for proxy in proxies]

        with open(filename, 'w') as proxy_file:
            json.dump(proxy_json, proxy_file)
