from bs4 import BeautifulSoup 
import requests

res = requests.get('http://127.0.0.1:5000/pokered').content

soap = BeautifulSoup(res,'html.parser')

print(soap)
