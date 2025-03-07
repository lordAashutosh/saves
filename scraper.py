# import requests
# from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from store import insert_job_data
search_term = input("What do you want to search job for\n").lower()
url = f'https://weworkremotely.com/remote-jobs/search?term={search_term}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
job_listings = soup.find_all('li', class_='feature')


if len(job_listings) < 1:
    print(f"Sorry man there is no job with keyword {search_term}")

fetched_jobs = []
for job in job_listings:
    title_elem = job.find('span', class_='title')
    title = title_elem.text.strip()
    company_elem = job.find('span', class_='company')
    company = company_elem.text.strip()

    all_links = job.find_all('a', href=True)
    detail_url = f'https://weworkremotely.com/{all_links[1]["href"]}'


    data = {"job_title":title, "company":company, "detail_url":detail_url}
    # New Code
    job_detail_response = requests.get(detail_url, headers=headers)
    job_detail_soup = BeautifulSoup(job_detail_response.text, 'html.parser')

    apply_link_elem = job_detail_soup.find('a', id='job-cta-alt-2',href=True)
    if apply_link_elem:
        data['apply_link'] = apply_link_elem['href']
    else:
        data['apply_link'] = 'Not available'

    listing_tags = job_detail_soup.find_all('span', class_='listing-tag')
    data['salary'] = 'Not available'
    for each_tag in listing_tags:
        if "$" in each_tag.text:
            data['salary'] = each_tag.text
    
    insert_job_data(data['job_title'], data['company'], data['apply_link'], data['salary'])

    


