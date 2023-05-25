from requests import get
import re
from urllib.parse import urlparse

link = input().strip()
link_text = get(link).text

# Регулярка для поиска ссылок в тексте
pattern_link = re.compile(r""(?:<a.*?\shref=[\""'])(\S+?)(?=[\""'])"")
# Регулярка для вытаскивания домена из path, если netloc не найден в URL
pattern_path = re.compile(r""^[a-z]\S+?(?=\/)|^[a-z][\w\.]+"")
# Список со всеми спарсенными URL из текста
all_links = pattern_link.findall(link_text)
# Пустой список для хранения доменов из спарсенных URL
domains = list()

for item in all_links:
    parsed = urlparse(item)  # распарсенный URL
    if parsed.netloc:  # если netloc не пустой
        if not parsed.port:  # если netloc без порта
            domains.append(parsed.netloc)
        else:  # если netloc с портом, отрезаем порт
            domains.append(parsed.netloc.replace("":"" + str(parsed.port), """"))
    else:  # если netloc пустой
        parsed_path = pattern_path.search(parsed.path)  # регуляркой пытаемся достать домен из path
        if parsed_path:  # если получилось регуляркой достать домен из path, кладем домен в domains
            domains.append(parsed_path.group())

for domain in sorted(set(domains)):
    print(domain)
 