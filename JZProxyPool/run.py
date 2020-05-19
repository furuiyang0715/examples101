from proxypool.api import app
from proxypool.schedule import Schedule


def main():

    # 爬取并向代理队列中添加代理
    # 定时校验代理的有效性
    s = Schedule()
    s.run()

    # 运行起 web 服务
    app.run(host="0.0.0.0", port=8888)


if __name__ == '__main__':
    main()
