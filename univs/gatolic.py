from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://ipsi.catholic.ac.kr"
    notice_url = "/pages/?p=15&b=B_1_1&cate=%C1%A4%BD%C3"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        data = univ_info2dict("가톨릭대", anchor.text.strip(), prefix_url, notice_url)
        notice_list.append(data)
    return notice_list
