import re
from bs4 import BeautifulSoup

def remove_first_dotdot_slash(html_content):
    # Функция для замены первого вхождения '../' на ''
    def replace_first(match):
        return match.group(0)[3:]  # Удаляем первые '../'

    # Регулярное выражение для поиска всех вхождений '../'
    pattern = r'(\.\./)'

    # Заменяем только первое вхождение '../' в каждой строке
    modified_content = re.sub(pattern, replace_first, html_content, count=1)

    return modified_content

def process_html_file(input_file, output_file):
    # Читаем HTML файл
    with open(input_file, 'r', encoding='windows-1251') as file:
        html_content = file.read()

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Обрабатываем все теги с атрибутами, содержащими пути
    for tag in soup.find_all(True):  # True находит все теги
        for attr in tag.attrs:
            if isinstance(tag[attr], str):
                # Обрабатываем атрибут, если он содержит путь
                tag[attr] = remove_first_dotdot_slash(tag[attr])

    # Записываем обработанный HTML в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Пример использования
input_filename = 'D:\\siteindex.txt'  # Укажите путь к вашему входному HTML файлу
output_filename = 'D:\\output.txt'  # Укажите путь к выходному HTML файлу
process_html_file(input_filename, output_filename)