import os

env = os.environ.get


# Redis数据库的地址和端口
HOST = env("HOST", '192.168.199.228')
PORT = env("PORT", 6379)

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = env("PASSWORD", '')

# 获得代理测试时间界限
GET_PROXY_TIMEOUT = env("get_proxy_timeout", 9)

# 代理池数量界限
POOL_LOWER_THRESHOLD = env("POOL_LOWER_THRESHOLD", 20)
POOL_UPPER_THRESHOLD = env("POOL_UPPER_THRESHOLD", 100)

# 检查周期
VALID_CHECK_CYCLE = env("VALID_CHECK_CYCLE", 60)
# POOL_LEN_CHECK_CYCLE = env("POOL_LEN_CHECK_CYCLE", 20)
POOL_LEN_CHECK_CYCLE = env("POOL_LEN_CHECK_CYCLE", 5)

# 测试API，用百度来测试
TEST_API = env("TEST_API", 'http://www.baidu.com')


if __name__ == "__main__":
    # print(HOST)
    # print(PORT)
    # print(PASSWORD)
    # print(get_proxy_timeout)
    # print(POOL_LOWER_THRESHOLD)
    # print(POOL_UPPER_THRESHOLD)
    # print(VALID_CHECK_CYCLE)
    # print(POOL_LEN_CHECK_CYCLE)
    # print(TEST_API)

    import sys
    mod = sys.modules[__name__]
    attrs = dir(mod)
    attrs = [attr for attr in attrs if not attr.startswith("__") and attr.isupper()]
    # print(attrs)
    for attr in attrs:
        print(getattr(mod, attr))
