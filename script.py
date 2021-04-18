import requests, zipfile, io
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import redis
import csv

url = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
headers={'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=headers) # Fetching Url for getting link of download file
web_byte = urlopen(req).read() 
webpage = web_byte.decode('utf-8')

soup = BeautifulSoup(webpage,features="lxml") 
file_url = soup.find("a",{"id":"ContentPlaceHolder1_btnhylZip"}).get('href') # Finding link of file to download

file_req = requests.get(file_url, headers=headers, stream=True) # Downloading File
z = zipfile.ZipFile(io.BytesIO(file_req.content))
z.infolist()[0].filename = "Today.csv"
z.extract(z.infolist()[0])  # Extracting zip file and saving with name of Today.csv

redis_host = "localhost"
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port) #Redis Connection object

with open("Today.csv") as file: # Storing file data in redis
    for record in list(csv.DictReader(file)):
        name = record['SC_NAME'].strip()
        value = {'Name':name, 'Code':record['SC_CODE'],'Open': record['OPEN'],'Close':record['CLOSE'],'High':record['HIGH'],'Low':record['LOW']}
        r.hmset(name,value)