from urllib.request import urlopen
from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url: str, timeout: int = 2) -> bool:
    """
    Return True if the target URL is online.
    Raise an exception
    :param url:
    :param timeout:
    :return:
    """
    error = Exception('unknown error')
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request('HEAD', '/')
            return True
        except Exception as ex:
            error = ex
            print(error)
        finally:
            connection.close()
    raise error


if __name__ == '__main__':
    print(site_is_online('www.bourseview.com'))
    print(site_is_online('www.yechizalaki.com'))
    # response = urlopen('https://python.org')
    # print(response.read())
    # connection = HTTPConnection('varzesh3.com', port=80, timeout=10)
    # connection.request("HEAD", '/')
    #
    # response = connection.getresponse()
    # print(response.getheaders())
