
import requests
from bs4 import BeautifulSoup
search_term = input("What do you want to search job for\n").lower()
url = f'https://weworkremotely.com/remote-jobs/search?term={search_term}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

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
    fetched_jobs.append(data)

for index,job in enumerate(fetched_jobs):
    print(f"{index+1}. {job['job_title']} @ {job['company']}")

job_select = int(input("Enter the job number you want to view more information of\n"))
job_index = job_select - 1

print(f"Thank you. You selected {fetched_jobs[job_index]['job_title']} at {fetched_jobs[job_index]['company']}. I will show you the details of this job now")
print(f"You can view more detail at {fetched_jobs[job_index]['detail_url']}")

# Hit Detail URl
# Parse the response.text
# Find apply link with href=True and display the URL


