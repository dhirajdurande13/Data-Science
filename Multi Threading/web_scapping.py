'''
  urls for the web scrapping:
  
  https://python.langchain.com/docs/introduction/
  
  https://python.langchain.com/docs/concepts/
  
  https://python.langchain.com/docs/tutorials/
'''


urls=[
    
    'https://python.langchain.com/docs/introduction/',
  
  'https://python.langchain.com/docs/concepts/',
  
  'https://python.langchain.com/docs/tutorials/'
]
import requests
import threading
from bs4 import BeautifulSoup
def fetch_content(url):
    responce=requests.get(url)
    soup=BeautifulSoup(responce.content,'html.parser')
    # print(f"{soup.text} from {url}")
    print(f"Characters : {len(soup.text) } from {url}")
    
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
    
print("All Web Pages are Fetched")