import requests
from bs4 import BeautifulSoup as BS

response = requests.get(url="https://docs.zigzag.exchange/zigzag-exchange/zksync-market-maker-airdrop")
soup = BS(response.text)

result = soup.findAll("tr", "r-1oszu61 r-1xc7w19 r-1phboty r-1yadl64 "
                            "r-deolkf r-6koalj r-1mlwlqe r-1q142lx r-crgep1 "
                            "r-ifefl9 r-bcqeeo r-t60dpp r-bnwqim r-417010 r-18u37iz")

total_zz = 0
total_user = 0

with open('snapshot.md', 'w') as file:
    file.write("| **account_id** | **trade_count** | **zz_amount** |\n"
               "|----------------|-----------------|---------------|\n")

for element in result:
    content = element.contents

    account_id = 0
    trade_count = 0
    zz_amount = 0.0

    try:
        account_id = int(element.contents[0].text)
        trade_count = int(element.contents[1].text)
        zz_amount = float(element.contents[2].text)
    except:
        pass

    if account_id != 0 and trade_count != 0 and zz_amount != 0.0:
        total_zz += zz_amount
        total_user += 1

        with open('snapshot.md', 'a') as file:
            file.write('| ' + str(account_id) + ' | ' + str(trade_count) + ' | ' + str(zz_amount) + ' |\n')

with open('snapshot.md', 'a') as file:
    file.write(f'<br>total_user: {total_user}.<br>total_zz: {total_zz}.')
