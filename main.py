from bs4 import BeautifulSoup
import requests
import time

control = 0
unfamiliar_skills = []

print('Do you want to add skills you are unfamiliar with? Type "yes" or "no"')
if input('>') == 'no':
    control = 1

while control == 0:
    print('Put some skill that you are not familiar with')
    unfamiliar_skills.append(input('>'))
    print('Do you want to add another unfamiliar skill? Type "yes" or "no"')
    choice = input('>')
    if choice == 'no':
        break

print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        time_posted = job.find('span', class_='sim-posted').span.text
        if time_posted.find('few') == -1:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            for bad_skill in unfamiliar_skills:
                if bad_skill in skills:
                    break

            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()}\n')
                f.write(f'Required skills: {skills.strip()}\n')
                f.write(f'Link: {more_info}\n')

            print(f'File saved: {index}.txt')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
