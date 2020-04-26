"""Test module for the `Proxy` class"""

from scraproxy.proxy import Proxy


def test_proxy_url():
    """Tests the proxy class"""

    proxy = Proxy('192.168.1.1', port=8080, https=True)

    assert proxy.url == 'https://192.168.1.1:8080'


def test_proxy_dict():
    """Test the method `to_dict` of the `Proxy` class"""

    proxy = Proxy('192.168.1.1', port=8080, https=True)
    proxy_dict = proxy.to_dict()

    assert len(proxy_dict) == 2
    assert 'http' in proxy_dict
    assert 'https' in proxy_dict
    assert proxy_dict['http'] == 'http://192.168.1.1:8080'
    assert proxy_dict['https'] == 'https://192.168.1.1:8080'


def test_proxy_repr():
    """Tests the `__repr__` method of the `Proxy` class"""

    proxy = Proxy('192.168.1.1', port=8080, https=True, last_checked=60)

    assert repr(proxy) == '<Proxy https://192.168.1.1:8080 checked 60 seconds ago>'
