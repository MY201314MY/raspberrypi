import requests
from bs4 import BeautifulSoup

movie_list=[]

target = 'https://movie.douban.com/top250'
headers={
    }
r = requests.get(url=target)
r.encoding='uft-8'
bf = BeautifulSoup(r.text,'html5lib')
list = bf.find_all('div', class_ = 'hd')
for each in list:
    movie = each.a.span.text.strip()
    movie_list.append(movie)
print(movie_list)

for i in range(0, len(movie_list)):
    print(movie_list[i])

