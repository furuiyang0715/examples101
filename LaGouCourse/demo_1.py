import requests

proxies = {
  'http': 'http://10.10.10.10:1080',
  'https': 'http://10.10.10.10:1080',
}

requests.get('https://httpbin.org/get', proxies=proxies)