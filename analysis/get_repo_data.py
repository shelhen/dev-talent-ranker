# -*- encoding: utf-8 -*-
"""
--------------------------------------------------------
@File: get_repo_data.py
@Project: dev-talent-ranker 
@Time: 2024/10/25   00:20
@Author: hengheng.xie
@Email: shelhen@163.com
@Software: PyCharm 
--------------------------------------------------------
# @Brief: 获取GitHub项目信息脚本
"""
# from typing import List, Optional
from typing import Union, Iterable
import os
import requests


def load_urls(years: Iterable[int], months: Iterable[int]) -> Union[str, Iterable[str]]:
    template = 'https://data.gharchive.org/{0}-{1:02}-{2:02}-{3:02}.json.gz'
    for year in years:
        for month in months:
            for day in range(1, 3):
                for hour in range(10, 24):
                    yield template.format(year, month, day, hour)


def download_github_repo_data(urls: Iterable[str]) -> None:
    for url in urls:
        file_name = url.split('/')[-1]
        resp = requests.get(url)
        if resp.status_code == 404:
            print(f'404 Error: {url}')
        else:
            print(url)
            with open(os.path.join('repo_data', file_name), 'wb') as gf:
                gf.write(resp.content)
    # https://data.gharchive.org/2021-11-21-0.json.gz
    # https://data.gharchive.org/2024-09-29-11.json.gz


if __name__ == '__main__':
    _urls = load_urls(years=(2024, ), months=(9, ))
    download_github_repo_data(_urls)
