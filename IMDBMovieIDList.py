# %%
import csv
import urllib.request  # Import the correct library for opening URLs

# Define the CSV file path (replace with your actual file path)
csv_file_path = "IMDB_Movie_list.csv"  # Update with your CSV file name

# Open the CSV file in read mode with error handling
try:
    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        movie_names = []  # Create an empty list to store items from CSV

        # Read each row from the CSV and append items to the list
        for row in reader:
            movie_names.append(row[0])  # Assuming the first column contains items

except OSError as e:
    print("Error opening CSV file:", e)
    exit()  # Exit the program if there's an error

# Open the CSV file in write mode with error handling (same as before)
# ... (rest of the code remains the same, starting with `try:`)

print("Items saved successfully (or errors logged) to 'IMDB_Movie_list.csv'")

# %%

print(movie_names)

# %%


import requests
from bs4 import BeautifulSoup

# movie_names = ["TheBeekeeper", "Batman"]
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


# %%


# %%



