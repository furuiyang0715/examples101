from setuptools import setup

setup(
    name='proxy-pool',
    version='1.0.0',
    description='High performance proxy pool',
    long_description='A proxy pool project',
    author=['jz_developer'],
    author_email='ruiyang0715@gmail.com',
    # url='',
    packages=[
        'proxy-pool'
    ],
    py_modules=['run'],
    include_package_data=True,
    platforms='any',
    # 打包时需要安装的依赖
    install_requires=[
        'aiohttp',
        'requests',
        'flask',
        'redis',
        'pyquery'
    ],
    entry_points={
        'console_scripts': ['proxy_pool_run=run:cli']
    },
    license='apache 2.0',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)