"""This module contains a class to represent proxies"""


class Proxy:
    """Class representing a proxy"""

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
