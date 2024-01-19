import requests
response = requests.get("https://sitare.org/")
raw_content = response.text
# print(raw_content)

title_start = raw_content.find("<title>") + len("<title>")
title_end = raw_content.find("</title>")
title = raw_content[title_start:title_end]
print(title)

body_start = raw_content.find("<body>") + len("<body>")
body_end = raw_content.find("</body>")
body_raw_content = raw_content[body_start:body_end]
# print(body_raw_content)
# print(type(body_raw_content))
# print(len(body_raw_content))


body = []
while len(body_raw_content) > 1:
    s = body_raw_content.find("<p")
    x = body_raw_content[s:].find(">")
    e = body_raw_content[s+x:].find("</p")
    content = body_raw_content[s+x: e]

    trimmed_content = content.strip("'>\r\n ")

    if content != '':
        body.append(trimmed_content)

    body_raw_content = body_raw_content[e:]

for i in body:
    print(i)




link = []
while len(body_raw_content) > 1:
    s = body_raw_content.find("http")
    e = body_raw_content[s:].find('"')
    link.append(body_raw_content[s :s + e])

    body_raw_content = body_raw_content[s + e+1:]

for j in link:
    print(j)

