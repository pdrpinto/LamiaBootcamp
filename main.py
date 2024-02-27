from bs4 import BeautifulSoup
import requests

while True:
    print('What kind of jobs do you want to search?')
    control = 0
    unfamiliar_skills = []
    str1 = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords='
    str_user = input('>').replace(' ', '+')
    str2 = '&txtLocation='
    url_query = str1 + str_user + str2

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

    html_text = requests.get(url_query).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        unfamiliar_skill_found = False
        time_posted = job.find('span', class_='sim-posted').span.text
        if time_posted.find('few') == -1:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            for bad_skill in unfamiliar_skills:
                if bad_skill in skills:
                    unfamiliar_skill_found = True
                    break

            if not unfamiliar_skill_found:
                print('------------------------------------------------------')
                print(f'Company Name: {company_name.strip()}')
                print(f'Required skills: {skills.strip()}')
                print(f'Link: {more_info}')
                print('------------------------------------------------------')

                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required skills: {skills.strip()}\n')
                    f.write(f'Link: {more_info}\n')
                # print(f'File saved: {index}.txt')

    print('Do you want to make another search?')
    option = input('Y/N: ')
    if option.lower() != 'y':
        break
