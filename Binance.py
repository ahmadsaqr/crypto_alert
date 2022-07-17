from bs4 import BeautifulSoup
import time,re,schedule
from requests_html import HTMLSession



r=HTMLSession().get("https://www.binance.com/en/support/announcement/c-48?navId=48")
r=r.html
r= BeautifulSoup(r.text, "html.parser")

lastlist=re.search(r"Binance Will List\s[A-z0-9 ]*\s\(\w*\)",r.get_text()).group()


lastlist=re.search(r"\([A-z0-9 ]*\)",lastlist ).group()
# print(lastlist)

def check():
        
    if lastlist  != "(ANY)" : #last coin  to listed on binanace should not be equal to (ANY)         
        print('dsds')
        from server import server
        server(f"Binance will list {lastlist}", 'mobile')   
        # time.sleep(1000)


schedule.every(1).seconds.do(check)


while True:
    schedule.run_pending()
        
