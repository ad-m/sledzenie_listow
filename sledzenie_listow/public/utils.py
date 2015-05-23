from bs4 import BeautifulSoup
from requests import Session
from ..extensions import cache
# Settings
URL = 'http://emonitoring.poczta-polska.pl/wssClient.php'

# Init
SESSION = Session()


def get_number(real_number, s=None):
    s = s or Session()
    soup = BeautifulSoup(s.post(URL, data={'n': real_number}).text.encode('utf8'))
    sledzenie = soup.find(id='sledzenie_td')
    if sledzenie:
        return {'no': real_number, 'meta': sledzenie, 'history': soup.find(id='zadarzenia_td')}
    return False


def quest_number(nake_number, s=None):
    key = "nake_number=%s" % (nake_number)
    rv = cache.get(key)
    if rv is None:
        for i in range(0, 10):
            data = get_number("00" + str(nake_number) + str(i), s)
            if data:
                rv = data
                break
        cache.set(key, rv, timeout=60*60*6)  # 6 hours cache
    return rv


def quest_range(start_string='00559007734046803928', end_string='0055900773404680394', s=None):
    nake_start = int(start_string[0:19])
    nake_end = int(end_string[0:19])
    if nake_end-nake_start >= 50:
        return []
    result = []
    for x in range(nake_start, nake_end):
        result.append(quest_number(x))
    return result
