import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://myanimelist.net/topanime.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 safari/537.36"
}

print("Initiating connection to MyAnimeList...")

response = requests.get(url, headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

anime_rows = soup.find_all('tr', class_='ranking-list')

extracted_data = []

print(f"Found {len(anime_rows)} anime on the page. Extracting data...")

for row in anime_rows:
    rank_tag = row.find('td', class_='rank ac')
    rank = rank_tag.find('span').text.strip()

    title_tag = row.find('div', class_='di-ib clearfix')
    title = title_tag.find('a').text.strip()

    score_tag = row.find('td', class_='score ac fs14')
    score = score_tag.find('span').text.strip()

    anime_info = {
        "Rank": rank,
        "Title": title,
        "Score": score
    }
    extracted_data.append(anime_info)

df=pd.DataFrame(extracted_data)
df.to_csv("MyAnimeList_TopAnime.csv", index=False)

print("Scraping complete! Data successfully saved to MyAnimeList_TopAnime.csv")