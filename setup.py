from setuptools import setup, find_packages
import os


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name="dedup-img",
    version="1.0.2",
    author='cjlmonster',
    author_email='cjlmonster@163.com',
    description='imagededup图片查重封装使用',
    long_description=read_file('readme.md'),
    long_description_content_type="text/markdown",
    platforms='python3',
    url='https://cjlmonster.cn/python/dedupimg/',

    # 包含所有src中的包，但排除tests包
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_dir={'': 'src'},  # 告诉distutils包都在src下
    package_data={
        # 包含dedup包templates文件夹中的 *.html文件
        'dedup': ['templates/*.html'],
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt']

    },
    exclude_package_data={
        'dedup': ['templates/login.html']
    },
    python_requires='>=3',
    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=[
        'imagededup >= 0.2.2',
        'flask >= 2.0.1',
        # 'pillow >= 6.2.2, < 7.0.0'
    ],
    entry_points={
        'console_scripts': [
            'dedup = dedup.cmd:main',
            'flask-web = dedup.webapp:main',
        ],
        # 'gui_scripts': [
        #     'baz = tests:tests',
        # ]
    }
)
