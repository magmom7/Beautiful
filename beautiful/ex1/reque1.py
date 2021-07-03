import requests
url = "https://comic.naver.com/webtoon/weekday.nhn"
response = requests.get(url, verify=False)
data = response.text
print(data)
