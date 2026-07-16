import http.cookiejar, urllib.request, urllib.parse, re
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
url = 'http://127.0.0.1:8001/admin/login/?next=/admin/'
html = opener.open(url).read().decode('utf-8','ignore')
token = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html).group(1)
data = urllib.parse.urlencode({'username':'admin','password':'AdminPass123','csrfmiddlewaretoken':token,'next':'/admin/'}).encode()
req = urllib.request.Request(url, data=data, headers={'Referer':url})
resp = opener.open(req)
page = opener.open('http://127.0.0.1:8001/admin/members/member/')
print(page.getcode())
print(page.read(1200).decode('utf-8','ignore'))
