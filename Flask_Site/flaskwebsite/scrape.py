# Fabricio Zuniga
# July 14, 2021
# Forex Price Pair Tool
# MODIFY EXCEPTIONS!

from bs4 import BeautifulSoup
import requests
import csv

def csv_maker(pair_name=None, bid_price=None, ask_price=None, high_price=None, low_price=None, percent_change=None):
    csv_file = open("forex_stats.csv", "w")

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Pair Name", "Bid Price", "Ask Price", "High Price", "Low Price", "Percent Change"])

    count = 0
    while(count < len(pair_name)):
        csv_writer.writerow([pair_name[count], bid_price[count], ask_price[count], high_price[count], low_price[count], percent_change[count]])
        count += 1

    csv_file.close()

def average_calculate(high_price=None, low_price=None):
    average_price = []
    high_no_comma = []
    low_no_comma = []

    for element in range(0, len(high_price)):
        try:
            no_comma_h = high_price[element].replace(',', '')
            high_no_comma.append(no_comma_h)
            no_comma_l = low_price[element].replace(',', '')
            low_no_comma.append(no_comma_l)
        except Exception as e:
            print("Comma did not exist or could not be removed/replaced")

    float_high = [float(i) for i in high_no_comma]
    float_low = [float(i) for i in low_no_comma]

    for element in range(0, len(high_no_comma)):
        print(type(float_high[element]))
        print(type(float_low[element]))
        print("\n")
        average = (float_high[element] + float_low[element]) / 2.0
        average_price.append(average)

    return average_price

#investing.com - website for Forex Trade Prices
#header to HTML request modified to avoid 404 Error
url = "https://www.investing.com/currencies/streaming-forex-rates-majors"
mod_headers = {"User-Agent": "Mozilla/5.0"}

#send request to target
source = requests.get(url, headers=mod_headers).text

#BeautifulSoup source created
soup = BeautifulSoup(source, "html.parser")
#table contains table information
table = soup.find(id="cross_rates_container", class_="js-ga-on-sort")

#lists for table information
pair_name = []
bid_price = []
ask_price = []
high_price = []
low_price = []
percent_change = []

#begin parsing information onto appropriate lists
#trade pair name
for name in table.find_all(class_="bold left noWrap elp plusIconTd"):
    try:
        pair_name.append(name.text)
    except:
        print("Could not append")

#bid price
for bid in table.select('td[class*="-bid"]'):
    try:
        bid_price.append(bid.text)
    except:
        print("Error: list could not append element")

#ask price
for ask in table.select('td[class*="-ask"]'):
    try:
        ask_price.append(ask.text)
    except:
        print("Error: list could not append element")

#high price
for high in table.select('td[class*="-high"]'):
    try:
        high_price.append(high.text)
    except:
        print("Error: list could not append element")

#low price
for low in table.select('td[class*="-low"]'):
    try:
        low_price.append(low.text)
    except:
        print("Error: list could not append element")

#percent change from yesterday's high price
for percent in table.select('td[class*="-pcp"]'):
    try:
        percent_change.append(percent.text)
    except:
        print("Error: list could not append element")

# print(pair_name)
# print(ask_price)
# print(bid_price)
# print(high_price)
# print(low_price)
# print(percent_change)

csv_maker(pair_name, ask_price, bid_price, high_price, low_price, percent_change)
avg = average_calculate(high_price, low_price)
print(avg)
