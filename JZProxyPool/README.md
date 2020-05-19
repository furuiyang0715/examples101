### 安装

#### 本地
```python
# (1) 安装依赖 
pip install -r requirements.txt 

# (2) 配置环境变量 setting.py 
# PASSWORD为Redis密码，如果为空，则设置为None

# (3) 开启服务 
cd proxypool 
python run.py 

```

#### 打包
```python
python setup.py install

```

### 使用示例 
```python
examples/*
```

### 各模块功能
- getter.py

    爬虫模块

- class proxypool.getter.FreeProxyGetter

    爬虫类，用于抓取代理源网站的代理，用户可复写和补充抓取规则。

- schedule.py

    调度器模块

- class proxypool.schedule.ValidityTester

    异步检测类，可以对给定的代理的可用性进行异步检测。

- class proxypool.schedule.PoolAdder

    代理添加器，用来触发爬虫模块，对代理池内的代理进行补充，代理池代理数达到阈值时停止工作。

- class proxypool.schedule.Schedule

    代理池启动类，运行RUN函数时，会创建两个进程，负责对代理池内容的增加和更新。

- db.py

    Redis数据库连接模块

- class proxypool.db.RedisClient

    数据库操作类，维持与Redis的连接和对数据库的增删查该，

- error.py

    异常模块

- class proxypool.error.ResourceDepletionError

    资源枯竭异常，如果从所有抓取网站都抓不到可用的代理资源，则抛出此异常。

- class proxypool.error.PoolEmptyError

    代理池空异常，如果代理池长时间为空，则抛出此异常。

- api.py

    API模块，启动一个Web服务器，使用Flask实现，对外提供代理的获取功能。

- utils.py
    
    工具箱

- setting.py
    
    设置

### docker 部署
需要指明 redis 的相关配置 
```shell script
docker build -t registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/proxy_pool:v0.0.1 .

docker run -itd --name myproxy --env HOST=172.17.0.3 \
-p 8888:8888 registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/proxy_pool:v0.0.1

```

远程需要先开启一个 redis 服务
或者使用 docker-compose 部署




...


### 使用场景
（1） 现在的公司付费代理多人使用, 数量有限, 且有白名单。本地测试很不方便。可开启该线程池在本地进行测试。

（2） 可手动更改测试网站, 确保爬取的代理针对具体网站生效。 
（出现过代理对 百度 可用, 但是依然被特定的网站反 (例如 淘股吧)的情况。 

（3）即使网站未对 ip 设置严格反爬, 安全起见, 依然建议在请求的时候加一层代理。
