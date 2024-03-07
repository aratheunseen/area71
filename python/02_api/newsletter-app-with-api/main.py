import requests
import json

api_key = "06f80f04869d4d3db91252eb5c4b319c"
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-03-05&to=2024-03-05&sortBy=popularity&apiKey={api_key}"

# Make request
request = requests.get(url)

# Convert to json
content = request.json()

# Access content
for article in content['articles']:
    print(article['title'])
    print(article)
