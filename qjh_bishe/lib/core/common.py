from urllib.parse import urlparse


def urlsplit(url):
    """
    返回一个元祖将每个参数用my_Payload标记,后期替换参数
    :param url:
    :return:
    """
    domain = url.split("?")[0]
    _url = url.split("?")[-1]
    pararm = {}
    for val in _url.split("&"):
        pararm[val.split("=")[0]] = val.split("=")[-1]

    # combine
    urls = []
    for val in pararm.values():
        new_url = domain + _url.replace(val, "my_Payload")
        urls.append(new_url)
    return urls


def w8urlparse(url):
    domain = urlparse(url)
    # domain.netloc
    if domain.netloc is None:
        return None
    return domain.netloc
