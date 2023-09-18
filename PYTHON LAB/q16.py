import re

def validate_url(url):
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    if re.match(pattern, url):
        return True
    else:
        return False

# Test cases
urls = [
    "https://www.example.com",
    "http://www.example.com",
    "ftp://www.example.com",
    "https://example.com",
    "http://example.com",
    "ftp://example.com",
    "https://www.example.com/page",
    "http://www.example.com/page",
    "ftp://www.example.com/page",
    "https://www.example.com/page?param=value",
    "http://www.example.com/page?param=value",
    "ftp://www.example.com/page?param=value",
    "www.example.com",
    "example.com",
    "example",
    "https:/www.example.com",
    "https//www.example.com",
    "https://www.example com",
]

for url in urls:
    if validate_url(url):
        print(f"'{url}' is a valid URL.")
    else:
        print(f"'{url}' is not a valid URL.")