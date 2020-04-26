"""This module contains a class to represent proxies"""


import re
from .exceptions import InvalidProxyUrlException

URL_REGEX = re.compile(r'(http|https)://(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})')


class Proxy:
    """Class representing a proxy"""

    @staticmethod
    def from_url(url):
        """Creates a proxy instance from a URL string"""

        match = URL_REGEX.match(url)

        if not match or not all(match.group(i) for i in range(1, 3)):
            raise InvalidProxyUrlException(url)

        https = match.group(1) == 'https'
        ip_address = match.group(2)
        port = int(match.group(3))

        return Proxy(ip_address, port, https)

    def __init__(self, ip_address, port=80, https=False, last_checked=float('inf')):
        self.protocol = 'https' if https else 'http'
        self.ip_address = ip_address
        self.port = port
        self.last_checked = last_checked

    @property
    def url(self):
        """Returns the url of the proxy"""

        return f'{self.protocol}://{self.ip_address}:{self.port}'

    def to_dict(self):
        """Returns a dictionary representing the proxy"""

        proxy_dict = {'http': f'http://{self.ip_address}:{self.port}'}

        if self.protocol == 'https':
            proxy_dict['https'] = self.url

        return proxy_dict

    def __repr__(self):
        return '<Proxy {} checked {} seconds ago>'.format(self.url, self.last_checked)
