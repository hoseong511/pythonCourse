# requests 이용하기, indeed 를 beautifulsoup!
from indeed import extract_indeed_pages,extract_indeed_jobs

result = extract_indeed_pages()

extract_indeed_jobs(result)
