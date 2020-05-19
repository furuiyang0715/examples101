class ResourceDepletionError(Exception):
    # 全部的代理均不可用 资源耗尽的异常

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxy source is exhausted')


class PoolEmptyError(Exception):
    # 队列为空的异常

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxy pool is empty')