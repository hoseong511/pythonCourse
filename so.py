import requests
from bs4 import BeautifulSoup

search = input('SO! search for? ')
URL = f"https://stackoverflow.com/jobs?q={search}&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)
  print(last_page)
  # max_page = ceil(int(page[:-1])/LIMIT)
  return int(last_page)

def extract_job(html):
  title = html.find("div", {"class":"fl1"}).find("h2").find("a")["title"]  
  company, location= html.find("h3").find_all("span", recursive=False)
  company, location = company.get_text(strip=True), location.get_text(strip=True)
  job_id = html['data-jobid']
  return { 'title': title,
           'company':company, 
           'location':location,
           'apply_link':f"https://stackoverflow.com/jobs/{job_id}"
           }

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"scrapping SO page: {page+1}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:      
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)  
  return jobs