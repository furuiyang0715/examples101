import requests as req
from fake_useragent import UserAgent

ua = UserAgent()

headers = {"User-Agent": ua.random}

url = "https://www.zhihu.com/api/v4/members/traderusingpython/activities?limit=7&session_id=1204109748246929408&after_id=1581262642&desktop=True"

ret = req.get(url, headers=headers)

print(ret)
