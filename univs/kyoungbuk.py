
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://ipsi1.knu.ac.kr"
    notice_url = "/ipsi1/counsel/notice.jsp"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        data = univ_info2dict("경북대", anchor.text.strip(), prefix_url, notice_url)
        notice_list.append(data)

    return notice_list
