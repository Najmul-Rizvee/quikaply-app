import requests
from bs4 import BeautifulSoup

def get_jobs(title, location, mock=True):
    if mock:
        return [
            {"title": f"{title} Engineer", "company": "TechCorp", "location": location, "description": "Support clients with IT."},
            {"title": f"Senior {title}", "company": "Innovate Inc.", "location": location, "description": "Lead tech support initiatives."}
        ]

    headers = {"User-Agent": "Mozilla/5.0"}
    query = f"{title.replace(' ', '+')}&l={location.replace(' ', '+')}"
    url = f"https://ca.indeed.com/jobs?q={query}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []

    for div in soup.find_all("div", class_="job_seen_beacon")[:5]:
        try:
            job_title = div.find("h2").text.strip()
            company = div.find("span", class_="companyName").text.strip()
            loc = div.find("div", class_="companyLocation").text.strip()
            desc = div.find("div", class_="job-snippet").text.strip().replace("\n", "")
            jobs.append({"title": job_title, "company": company, "location": loc, "description": desc})
        except:
            continue
    return jobs
