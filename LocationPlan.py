# coding: utf-8
import csv
import json
import os

import sys

import chardet
import unirest

from Configs import config
from Utils.HttpUtils import post_json

reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG'] = 'SIMPLEFIED CHINESE_CHINA.UTF8'


def get_location():
    """
    读取文件
    :return:
    """
    cinema_lists = dict()
    csv_reader = csv.reader(open('cinema.csv'))
    for row in csv_reader:
        cinema_loc = row[0]
        cinema_name = row[1]
        cinema_lists[cinema_name] = cinema_loc

    return cinema_lists

def get_geocoding():

    """
    获取地理编码
    :return:
    """
    cinema_lists = get_location()
    print cinema_lists
    for cinema_loc in cinema_lists:
        # locs_geocoding = post_json(config.geocoding_url, cinema_loc)
        url = config.geocoding_url + cinema_loc
        locs_geocoding = post_json(url, cinema_loc)
        print url
        prov_result = unirest.post(url)
        # print locs_geocoding
        body = json.loads(prov_result.raw_body)
        # print body
if __name__ == '__main__':
    get_geocoding()
    # get_location()