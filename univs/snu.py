
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://admission.snu.ac.kr"
    notice_url = "/under/announcements"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        title = notice.find('td', {'class':'left'}).find('span').text.strip()

        data = univ_info2dict("서울대", title, prefix_url, link)
        notice_list.append(data)
    return notice_list
