import requests 
api_key = "bfdf7469835fe0607f6d26faec4aeae2a96c8"
url = input()
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL: ", shortened_url)
else:
    print("[!] Error Shortening URL: ", data)