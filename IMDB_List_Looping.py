

import requests
from bs4 import BeautifulSoup

movie_names = ["TheBeekeeper", "Batman"]
movie_ids = []

for movie_name in movie_names:
    
    url = f"https://www.imdb.com/find/?q={movie_name}&ref_=nv_sr_sm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a request to the IMDb search page
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    title_links = soup.find_all('a', href=lambda href: href and "/title/" in href)

    imdb_title_ids = [link['href'].split('/')[2] for link in title_links][1]
    
    movie_ids.append(imdb_title_ids)

print(movie_ids)
