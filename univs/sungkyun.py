
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://admission.skku.edu"
    notice_url = prefix_url + "/guide/dataroom.htm?etc1=notice"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("성균관대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)

    return notice_list
