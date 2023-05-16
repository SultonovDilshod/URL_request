import requests
API_key = "a743b2e2fd41482b93949c707d148e03"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-04-16&sortBy=publishedAt&apiKey=" \
      "a743b2e2fd41482b93949c707d148e03"
answer = requests.get(url=url)

content = answer.json()
for article in content['articles']:
    print(article['title'])
    print(article['description'])
