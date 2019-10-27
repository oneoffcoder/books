import urllib.request
import urllib.parse

# simple request
with urllib.request.urlopen('https://www.oneoffcoder.com/') as response:
    content = response.read()
    print(content)

# request with query string parameters
query_string_data = {
    'q': 'oneoffcoder',
    'sourceid': 'chrome',
    'ie': 'UTF-8'
}
query_string = urllib.parse.urlencode(query_string_data)
url = f'https://www.google.com/search?{query_string}'
data = urllib.request.urlopen(url)

# request with headers
query_string_data = {
    'q': 'oneoffcoder',
    'sourceid': 'chrome',
    'ie': 'UTF-8'
}
query_string = urllib.parse.urlencode(query_string_data).encode('ascii')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
url = 'https://www.google.com/search'

req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
    content = response.read()
