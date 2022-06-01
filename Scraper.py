# Scan popular job board websites like indeed, glassdoor, ziorecruiter, and linkedin with a specifc key term or phrase
# Retrun all postings from that keyword/phrase into a table
# Table will show the title, company, location, link, and the website its from
# Table can be sorted by location, title, site, etc.
# Table can check for and remove duplicate entries
# Maybe feature can show if we applied yet or not



import requests
from bs4 import BeautifulSoup
from helium import *


class Scraper:

    def __init__(self) -> None:
        pass

    def indeed():
        URL = "https://www.indeed.com/jobs?q=software%20developer&from=searchOnHP&vjk=76785349a91f064f&advn=9494391740989576"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="resultsBody")

        job_list = results.find_all("td", class_="resultContent")

        for job in job_list:
            title_element = job.find("a", class_="jcs-JobTitle")
            company_element = job.find("span", class_="companyName")
            location_element = job.find("div", class_="companyLocation")
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())
            print()



    def glassdoor():

        URL = "https://www.glassdoor.com/Job/software-developer-jobs-SRCH_KO0,18.htm?context=Jobs&clickSource=searchBox"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="MainCol")

        job_list = results.find_all("div", class_="d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0")

        for job in job_list:
            title_element = job.find("a", class_="jobLink job-search-key-1rd3saf eigr9kq1")
            company_element = job.find("a", class_="job-search-key-l2wjgv e1n63ojh0 jobLink")
            location_element = job.find("span", class_="css-1buaf54 pr-xxsm job-search-key-iii9i8 e1rrn5ka4")
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())
            print()



    def linkedin():

        URL = "https://www.linkedin.com/jobs/search?keywords=software%20developer&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="main-content")

        job_list = results.find_all("div", class_="base-search-card__info")
        for job in job_list:
            title = job.find("h3", class_="base-search-card__title")
            company = job.find("h4", class_="base-search-card__subtitle")
            location = job.find("span", class_="job-search-card__location")
            print(title.text.strip())
            print(company.text.strip())
            print(location.text.strip())
            print()



    def simply_hired():

        URL = "https://www.simplyhired.com/search?q=software+developer&l="

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        
        results = soup.find(id="job-list")
        
        job_list = results.find_all("div", class_="SerpJob-jobCard card")
        
        for job in job_list:
            title = job.find("a", class_="SerpJob-link card-link")
            company = job.find("span", class_="JobPosting-labelWithIcon jobposting-company")
            location = job.find("span", class_="jobposting-location")
            print(title.text.strip())
            print(company.text.strip())
            print(location.text.strip())
            print()



    def gov_jobs():

        URL = "https://www.governmentjobs.com/jobs?keyword=software+developer&location="

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        
        results = soup.find(id="job-list-container")
        
        job_list = results.find_all("li", class_="job-item")
        
        for job in job_list:
            title = job.find("a", class_="job-details-link")
            company = "Government"
            location = job.find("div", class_="primaryInfo job-location")
            print(title.text.strip())
            print(company)
            print(location.text.strip())
            print()
    
    indeed()
    glassdoor()
    linkedin()
    simply_hired()
    gov_jobs()

# Add regex to sort through data and find "entry" or "junior" positions
# Add data to sql database for manipulation(ie: checkmark box to signify applied or not, sort by(location))
