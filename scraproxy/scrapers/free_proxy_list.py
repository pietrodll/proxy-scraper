"""This module contains the `FreeProxyList` class"""

import re
from ..proxy import Proxy
from .scraper import ProxyScraper


LAST_CHECKED_REGEX = re.compile(
    r'(?:(\d+)\s+hours?)?(?:(\d+)\s+minutes?)?(?:(\d+)\s+seconds?)?\s+ago'
)


def parse_proxy(table_row):
    """Parses a row of the table displayed on the website to get the data of the proxy"""

    https = table_row.contents[6].string == 'yes'
    ip_address = table_row.contents[0].string
    port = table_row.contents[1].string

    match = LAST_CHECKED_REGEX.match(table_row.contents[7].string)
    last_checked = sum(int(match.group(i + 1) or 0) * 60 ** (2 - i) for i in range(3))

    return Proxy(ip_address, port=port, https=https, last_checked=last_checked)


class FreeProxyList(ProxyScraper):
    """Class to get the proxies from `free-proxy-list.net`"""

    website_url = 'https://free-proxy-list.net'

    def load_proxies(self):
        """Loads the proxies from `free-proxy-list.net`"""

        soup = self._get_soup()
        proxy_table = soup.find(id='proxylisttable')
        proxies = []

        for row in proxy_table.find_all('tr'):
            if row.find('td'):
                proxies.append(parse_proxy(row))

        self._proxies = proxies
