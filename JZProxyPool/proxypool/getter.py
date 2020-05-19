import sys

from pyquery import PyQuery as pq
import re

from proxypool.utils import get_page


class ProxyMetaclass(type):
    """
        元类，在FreeProxyGetter类中加入
        __CrawlFunc__和__CrawlFuncCount__
        两个参数，分别表示爬虫函数，和爬虫函数的数量。
    """

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class FreeProxyGetter(object, metaclass=ProxyMetaclass):
    # 设置元类 植入爬虫函数以及爬虫函数的数量
    # callback 指的是实现的具体的爬虫函数
    # eval("self.{}()".format(callback)) 指执行每一个爬虫函数之后获取到的代理
    def get_raw_proxies(self, callback):
        proxies = []
        print('Callback', callback)
        for proxy in eval("self.{}()".format(callback)):
            print('Getting', proxy, 'from', callback)
            proxies.append(proxy)
        return proxies

    def crawl_jz_open_kuai(self):
        # 经传的开放快代理接口
        url = "http://ent.kdlapi.com/api/getproxy/?orderid=924829619838717&num=80&protocol=1&method=2&an_an=1&an_ha=1&sep=1"
        html = get_page(url)
        proxies = html.split("\r\n")
        for proxy in proxies:
            yield proxy

    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #     # \s* 匹配空格，起到换行作用
    #     re_ip_adress = ip_adress.findall(str(html))
    #     for adress, port in re_ip_adress:
    #         result = adress + ':' + port
    #         yield result.replace(' ', '')

    def crawl_kuaidaili(self):
        # 针对某个网站获取代理具体抓取逻辑
        for page in range(1, 4):
            # 国内高匿代理
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            html = get_page(start_url)
            ip_adress = re.compile(
                '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
            )
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')

    def crawl_xicidaili(self):
        for page in range(1, 4):
            start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
            html = get_page(start_url)
            ip_adress = re.compile(
                '<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
            )
            # \s* 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')

    def crawl_daili66(self, page_count=4):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    # def crawl_data5u(self):
    #     for i in ['gngn', 'gnpt']:
    #         start_url = 'http://www.data5u.com/free/{}/index.shtml'.format(i)
    #         html = get_page(start_url)
    #         ip_adress = re.compile(
    #             ' <ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>'
    #         )
    #         # \s * 匹配空格，起到换行作用
    #         re_ip_adress = ip_adress.findall(str(html))
    #         for adress, port in re_ip_adress:
    #             result = adress + ':' + port
    #             yield result.replace(' ', '')

    def crawl_kxdaili(self):
        for i in range(1, 4):
            start_url = 'http://www.kxdaili.com/ipList/{}.html#ip'.format(i)
            html = get_page(start_url)
            ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s* 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')

    # def crawl_premproxy(self):
    #     for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
    #         start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(
    #             i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>')
    #             re_ip_adress = ip_adress.findall(str(html))
    #             for adress_port in re_ip_adress:
    #                 yield adress_port.replace(' ', '')

    # def crawl_xroxy(self):
    #     for i in ['CN', 'TW']:
    #         start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(
    #             i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress1 = re.compile(
    #                 "title='View this Proxy details'>\s*(.*).*")
    #             re_ip_adress1 = ip_adress1.findall(str(html))
    #             ip_adress2 = re.compile(
    #                 "title='Select proxies with port number .*'>(.*)</a>")
    #             re_ip_adress2 = ip_adress2.findall(html)
    #             for adress, port in zip(re_ip_adress1, re_ip_adress2):
    #                 adress_port = adress + ':' + port
    #                 yield adress_port.replace(' ', '')

    def crawl_jz_private_kuai(self):
        # 经传的付费私密快代理
        # 私密代理必须在白名单服务器上使用
        url = "https://dps.kdlapi.com/api/getdps/?orderid=934751511166930&num=20&pt=1&sep=1"
        html = get_page(url)
        proxies = html.split("\r\n")
        for proxy in proxies:
            yield proxy


if __name__ == "__main__":
    d = FreeProxyGetter()
    # ret = d.crawl_ip181()
    # ret = d.crawl_daili66()
    # ret = d.crawl_data5u()
    # ret = d.crawl_kxdaili()
    # ret = d.crawl_premproxy()
    # ret = d.crawl_xroxy()
    # ret = d.crawl_xicidaili()
    # ret = d.crawl_kuaidaili()
    ret = d.crawl_jz_open_kuai()
    # ret = d.crawl_jz_private_kuai()

    for r in ret:
        print(r)

    sys.exit(0)

    # just simple test
    _crawler = FreeProxyGetter()
    for callback_label in range(_crawler.__CrawlFuncCount__):
        callback = _crawler.__CrawlFunc__[callback_label]
        raw_proxies = _crawler.get_raw_proxies(callback)
        print(raw_proxies)