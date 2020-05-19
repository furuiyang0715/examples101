import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import HOST, PORT, PASSWORD


class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    def get(self, count=1):
        """
        get proxies from redis

        从队列的左边获取 count 个代理 默认只获取一个
        """
        proxies = self._db.lrange("proxies", 0, count - 1)
        self._db.ltrim("proxies", count, -1)
        return proxies

    def put(self, proxy):
        """
        add proxy to right top

        从队列的右边将代理加入
        """
        self._db.rpush("proxies", proxy)

    def pop(self):
        """
        get proxy from right.

        从队列的右端获取最新代理
        因为代理均从左拿出校验 校验成功的从右加入 因为最最右的一个极为最新可用代理
        """
        try:
            return self._db.rpop("proxies").decode('utf-8')
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        """
        get length from queue.

        获取代理池队列的长度
        """
        return self._db.llen("proxies")

    def flush(self):
        """
        flush db

        清空代理队列
        """
        self._db.flushall()


if __name__ == '__main__':
    conn = RedisClient()
    # conn.put(b"ruiyang")
    print(conn.pop())