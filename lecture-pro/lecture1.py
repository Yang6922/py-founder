import openpyxl
import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd


def fecth_table():
    url = "https://datatables.net/"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'PHPSESSID=7imt6n1a183pbr8oir04qodrid; dt-demo-scheme=auto',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com.hk/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    if response.status_code != 200:
        raise requests.RequestException(f"请求异常:{response.text}")
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())
    tables_document = soup.find('table', id="example")
    print(tables_document)
    header_list = tables_document.find("thead").find_all("th")
    print(header_list)
    titles_list = [head.text.strip() for head in header_list]
    print(titles_list)
    body_list = tables_document.find("tbody").find_all("tr")
    table_list = []
    for body_tr in body_list:
        detail_list = body_tr.find_all("td")
        td_data = []
        for detail in detail_list:
            td_data.append(detail.text.strip())
        print(td_data)
        table_list.append(td_data)
    print(table_list)
    wb = Workbook()
    worksheet = wb.active
    worksheet.title = "爬虫数据"
    worksheet.append(titles_list)
    for table in table_list:
        worksheet.append(table)

    wb.save("爬虫数据.xlsx")


if __name__ == '__main__':
    fecth_table()
