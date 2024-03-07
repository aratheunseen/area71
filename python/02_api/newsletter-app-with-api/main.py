import requests
import mailer

# Change NewsAPI.org key (Its a sample key)
api_key = "06f80f04869d4d3db91252eb5c4b319c"
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-03-05&to=2024-03-05&sortBy=popularity&apiKey={api_key}"

# Make request
request = requests.get(url)

# Convert to json
content = request.json()

# Access content
name = "The Newsletter"
message = ""
for article in content['articles']:
    if article['title'] is not None:
        message = message + article["title"] + "\n" + article["description"] + "\n"

message = message.encode("utf-8")

body = f"""\
Subject: Hello from {name}

{message}
"""
mailer.send_mail(body)