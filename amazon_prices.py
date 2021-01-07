import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os
import pathlib

URL = 'https://www.amazon.com.au/gp/product/B079HYCWR1/ref=ox_sc_act_title_1?smid=A2NLI3B5IXPZVP&psc=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

creditential_files_dir = str(pathlib.Path(__file__).parent.absolute()) + '\\data\\login_details.txt'


def send_mail(gmail, password, recipant_email, senders_email):
    print('sending gmail')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(gmail, password)
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
    body2 = title + part1 + price
    msg = f'subject: {subject}\n\n{body2}\n\n{body}'

    server.sendmail(recipant_email, senders_email, msg)
    print('GMAIL HAS BEEN SENT SUCSESSFULLY!')

    server.quit()


def check_price(g, p, re, se):
    print('checking price')
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price.replace('$', ''))
    if (converted_price <= 100.00):
        send_mail(g, p, re, se)
    else:
        print('still too expensive')


login_file = open(creditential_files_dir, "r")

if not os.path.exists(creditential_files_dir):
    print("login_details.txt does not exist, please full in login details")
    create_login_file = open("login_details.txt", "x")
    exit()
elif not os.path.getsize(creditential_files_dir) > 0:
    print("Theres no login information, please enter your login details")

login_file = open(creditential_files_dir, "r")
print("Got login details, initalizing.....")
line = login_file.readlines()

gmail = str(line[0])
password = str(line[1])
sender_email = str(line[2])

while True:
    check_price(gmail, password, gmail, sender_email)
    time.sleep(30)
