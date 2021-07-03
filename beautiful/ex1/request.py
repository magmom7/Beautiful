import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print(len(res.text))
print(res.text)

with open("go.html", "w", encoding="utf-8") as f:
    f.write(res.text)
