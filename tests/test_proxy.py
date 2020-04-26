"""Test module for the `Proxy` class"""

from pytest import raises
from scraproxy.proxy import Proxy, InvalidProxyUrlException


class TestProxy:
    """Tests the `Proxy` class"""

    def test_url(self):
        """Tests the proxy class"""

        proxy = Proxy('192.168.1.1', port=8080, https=True)

        assert proxy.url == 'https://192.168.1.1:8080'


    def test_dict(self):
        """Test the method `to_dict` of the `Proxy` class"""

        proxy = Proxy('192.168.1.1', port=8080, https=True)
        proxy_dict = proxy.to_dict()

        assert len(proxy_dict) == 2
        assert 'http' in proxy_dict
        assert 'https' in proxy_dict
        assert proxy_dict['http'] == 'http://192.168.1.1:8080'
        assert proxy_dict['https'] == 'https://192.168.1.1:8080'


    def test_repr(self):
        """Tests the `__repr__` method of the `Proxy` class"""

        proxy = Proxy('192.168.1.1', port=8080, https=True, last_checked=60)

        assert repr(proxy) == '<Proxy https://192.168.1.1:8080 checked 60 seconds ago>'


    def test_from_url(self):
        """Test the static method `from_url` of the `Proxy` class"""

        proxy = Proxy.from_url('https://192.168.1.1:8080')

        assert proxy.protocol == 'https'
        assert proxy.port == 8080
        assert proxy.ip_address == '192.168.1.1'

        with raises(InvalidProxyUrlException):
            Proxy.from_url('invalid_url')
