# coding: utf-8
import csv
import json
import os

import sys
import urllib2

import chardet
import unirest

from Configs import config
from Utils.HttpUtils import post_json

reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


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
        url = config.geocoding_url + cinema_loc
        prov_result = urllib2.urlopen(url).read()
        body = eval(prov_result)
        geocodes_list = body['geocodes'][0]
        location = geocodes_list['location']
        print location


def get_transit():
    """
    计算两个地理位置之间的交通方式
    :return:
    """
    origin = '116.481028,39.989643'
    destination = '116.419034,40.033411'
    transit_url = config.transit_url + 'origin=' + origin + '&destination=' + destination
    transit = urllib2.urlopen(transit_url).read()
    print transit


if __name__ == '__main__':
    # get_geocoding()
    # get_location()
    get_transit()