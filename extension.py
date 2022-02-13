"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        with open(f"{year}.html", "w") as file:
            file.write(str(soup))

        num_male = 0
        num_female = 0
        items = soup.find('table', {'class': 't-stripe'}).tbody.find_all('tr')
        for item in items[:-1]:
            num_male += int(item.text.split()[2].replace(',', ''))
            num_female += int(item.text.split()[4].replace(',', ''))
        print('Male Number: ' + str(num_male))
        print('Female Number: ' + str(num_female))


if __name__ == '__main__':
    main()
