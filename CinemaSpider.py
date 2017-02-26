# coding: utf-8
from bs4 import BeautifulSoup
import requests
import csv


url = "http://www.meituan.com/dianying/cinemalist/all/all/page{page}"

# 已完成的页数序号，初时为0
page = 0

csv_file = open("cinema.csv", "wb")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print "爬取: ", url.format(page=page)
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, "html.parser")

    cinema_list = html.select(".cinema-info__list > div")

    # 循环到第10页结束
    if page >= 10:
        break

    for cinema in cinema_list:
        cinema_name = cinema.select("a")[0].string.encode("utf8").strip()
        cinema_addr = cinema.select("dd")[0].string.encode("utf8").strip()  # strip()去空格
        csv_writer.writerow([cinema_name, cinema_addr])

csv_file.close()
