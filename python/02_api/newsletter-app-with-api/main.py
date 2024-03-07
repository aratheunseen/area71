import requests
import mailer

# Change NewsAPI.org key (Its a sample key)
api_key = "06f80f04869d4d3db91252eb5c4b319c"
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-03-05&to=2024-03-05&language=en&sortBy=popularity&apiKey={api_key}"

# Make request
request = requests.get(url)

# Convert to json
content = request.json()

# Access content
name = "The Newsletter"
message = ""
for article in content["articles"][:10]:
    if article['title'] is not None:
        message = f"{message}\n{article['title']}\n{article['description']}\n{article['url']}\n\n"

mail_body = f"""Subject: Latest update from {name}"\

{message}
"""
body = mail_body.encode('utf-8')

mailer.send_mail(body)

print(body.decode('utf-8'))