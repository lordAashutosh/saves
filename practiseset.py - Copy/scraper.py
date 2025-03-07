import requests
search_term = 'python'
url = f'https://weworkremotely.com/remote-jobs/search?term={search_term}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.content)
with open('dump.html', 'w') as file:
    file.write(str(response.content))