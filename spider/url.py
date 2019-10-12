import requests
from bs4 import BeautifulSoup
 
iurl = 'http://news.sina.com.cn/c/nd/2017-08-03/doc-ifyitapp0128744.shtml'
 
res = requests.get(iurl)
 
res.encoding = 'utf-8'
 
print(len(res.text))
 
soup = BeautifulSoup(res.text,'html.parser')
 
#标题
H1 = soup.select('#artibodyTitle')[0].text
print(H1)
#来源
time_source = soup.select('.time-source')[0].text
print(time_source)
 
#来源
origin = soup.select('#artibody p')[0].text.strip()
 
#原标题
oriTitle = soup.select('#artibody p')[1].text.strip()
print(oriTitle)
#内容
raw_content = soup.select('#artibody p')[2:19]
content = []
for paragraph in raw_content:
    content.append(paragraph.text.strip()) 
#责任编辑
ae = soup.select('.article-editor')[0].text
print(ae)
