from bs4 import BeautifulSoup
import requests
import time
from plyer import notification
def notify(title, message):
    notification.notify(title=title, app_icon='D:\Projects\Python Projects\PycharmProjects\hehe.ico',
                        message=message, timeout=2)
while True:
    url = 'https://www.x-rates.com/table/?from=USD&amount=1'
    data = requests.get(url).text
    d=[]
    soup = BeautifulSoup(data,'html.parser')
    for table in soup.find_all('tbody')[0].find_all('tr'):
        d.append((table.get_text().split()))
    for rate in d:
        if rate[0]!='Indian':
            continue
        print('USD vs INR:')
        print(f'1:{rate[2]}')
        notify('USD vs INR',f'1:{rate[2]}')
        time.sleep(1)


