
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://enter.jbnu.ac.kr/"
    notice_url = "bbs/board.php?bo_table=sub06_01&sca=수시%2F정시"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find_all('a')[1]
        link = anchor.attrs['href']
        data = univ_info2dict("전북대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)
    return notice_list
