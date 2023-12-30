from bs4 import BeautifulSoup

html_code = '<p><img src="image.jpg" alt="Example"></p>'

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Находим тег <p>
p_tag = soup.find('p')

# Находим тег <img> внутри <p>
img_tag = p_tag.find('img')

# Заменяем тег <p> тегом <img>
p_tag.replace_with(img_tag)

# Выводим измененный HTML
print(soup.prettify())
