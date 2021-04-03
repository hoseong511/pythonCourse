from bs4 import BeautifulSoup
import requests
import os

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("ul", {"class":"pagination-list"})

  links = pagination.find_all('a')
  page = []
  # 나는 전체 결과 수 에서 50을 나눠 나온 값에 올림한 값이 max!!
  for link in links:
    try:
      page.append(int(link.string))
    except:
      continue

  max_page = page[-1]
  return max_page

def extract_indeed_jobs(last_page):
  os.system('clear')
  # for pages in range(last_page):
  # result = requests.get(f"{INDEED_URL}&start={pages*LIMIT}")
  result = requests.get(f"{INDEED_URL}&start={0}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  # print(results)  
  for result in results:
    title = result.find("h2", {"class":"title"}).find('a')["title"]
    
    company = result.find("span", {"class":"company"}).text.strip()
    if company == "":
      company = "이름누락-----------------------------------------------------"
    print(f"{title}, {company}")
    
  

    
  return
