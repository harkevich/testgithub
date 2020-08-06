from bs4 import BeautifulSoup
import urllib.request
req = urllib.request.urlopen("https://www.belta.by/all_news/")
html = req.read()
soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='news_item lenta_item')
results = []
for item in news:
    title = item.find('span', class_='lenta_item_title').get_text(strip=True)
    desc = item.find('span', class_='lenta_textsmall').get_text(strip=True)
    # desc = item.find('h1', clashes_='hide').get_text(strip=True)
    # price = item.find('div', class_="b-item_ad_price").get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        # 'price': price,
        'href': href,

    })
f = open('news_abw_by.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(
        f'Новость № {i}\n\nНазвание:{item["title"]}\nОписание: {item["desc"]}\nСсылка:{item["href"]}\n\n********************\n\n')
    i += 1
f.close()


