# pip install beautifulsoup4
# pip install lxml
# Estes pacotes servem para extrair dados de páginas web.
# A principal diferença entre parsers HTML e XML é que em XML é mais apropriado para permitir que aplicações
# troquem e aloquem informações em sua estrutura em um jeito universalment compreendido.

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # Método find() acha a primeira instancia da tag fornecida, porem find_all() acha todas.
    tags = soup.find('h5')
    courses_html_tags = soup.find_all('h5')

    # for course in courses_html_tags:
    #     print(course.text)
    # print(courses_html_tags[0].text)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'Course name: {course_name} | Price: {course_price}')




