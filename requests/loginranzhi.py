import requests
import hashlib
import re

url = "http://127.0.0.1/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html"
r = requests.get(url)
pattern = "(?=v.random = \").*(?=;<)"
result = re.search(pattern,r.text).group()
random_str = result.replace('v.random = "','').replace('"','')

username='admin'
password = '1234'
password = hashlib.md5(hashlib.md5(hashlib.md5(random_str.encode('utf-8')) + username) + random_str)

