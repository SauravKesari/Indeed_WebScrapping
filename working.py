from matplotlib.pyplot import title
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
def extract(page):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url=f'https://in.indeed.com/jobs?q=python%20developer&l=Surat%2C%20Gujarat&start={page}'
    r=rq.get(url,header)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs=soup.find_all('div',class_='job_seen_beacon')
    for item in divs:
        title=item.find('a').text.strip()
        company=item.find('span',class_='companyName').text.strip()
        location=item.find('div',class_='companyLocation').text.strip()

        try:
            salary=item.find('div',class_='metadata salary-snippet-container').text.strip();
        except:
            salary=""

        job={
            'title':title,
            'company':company,
            'salary':salary,
            'location':location
        } 
        joblist.append(job)       
    return    

joblist=[]

for i in range(0,40,10):
    print(f'loading page {i}')
    c=extract(0)    
    transform(c)

df=pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')