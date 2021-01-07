import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.au/gp/product/B079HYCWR1/ref=ox_sc_act_title_1?smid=A2NLI3B5IXPZVP&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}



def send_mail():
    print('sending gmail')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('--your gmail--', '--password--')
    print('login successfully')

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    title = name.strip()
    print(title, '|', price)
    
    subject = 'hey, the price fell down (under $100)'
    body = 'check the amazon link: https://www.amazon.com.au/gp/product/B079HYCWR1/ref=ox_sc_act_title_1?smid=A2NLI3B5IXPZVP&psc=1'
    part1 = '|'
    body2 = title + part1 +price
    msg = f'subject: {subject}\n\n{body2}\n\n{body}'

    server.sendmail('--your gmail--', '--the gmail acc u want to send to--', msg)
    print('GMAIL HAS BEEN SENT SUCSESSFULLY!')

    server.quit()

def check_price():
    print('checking price')
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price =soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price.replace('$', ''))
    if(converted_price <= 100.00):
        send_mail()
    else:
        print('still too expensive')

while True:
    check_price()
    time.sleep(30)

