import requests

#This function will print title of any webpage.

def title(url):
    response = requests.get(url)
    raw_content = response.text
    
    title_start = raw_content.find("<title>") + len("<title>")
    title_end = raw_content.find("</title>")
    title = raw_content[title_start:title_end]
    print(title)




def body(url):
    response = requests.get(url)
    raw_content = response.text
    
    body_start = raw_content.find("<body>") + len("<body>")
    body_end = raw_content.find("</body>")
    body_raw_content = raw_content[body_start:body_end]

    body_list = []
    while len(body_raw_content) > 1:
        s = body_raw_content.find("<p")
        x = body_raw_content[s:].find(">")
        e = body_raw_content[s+x:].find("</p")
        content = body_raw_content[s+x: e]

        trimmed_content = content.strip("'>\r\n ")

        if content != '':
            body_list.append(trimmed_content)

        body_raw_content = body_raw_content[e:]

    for i in body_list:
        print(i)




def links(url):
    response = requests.get(url)
    raw_content = response.text
    
    body_start = raw_content.find("<body>") + len("<body>")
    body_end = raw_content.find("</body>")
    body_raw_content = raw_content[body_start:body_end]

    link = []
    while len(body_raw_content) > 1:
        s = body_raw_content.find("http")
        e = body_raw_content[s:].find('"')
        link.append(body_raw_content[s :s + e])

        body_raw_content = body_raw_content[s + e+1:]

    for j in link:
        print(j)







url = input("Enter your Url with https :")

inp = input("What you want to see in your website, Title : 1, Body : 2, Links: 3 :")

if int(inp) == 1:
    title(url)

elif int(inp) == 2:
    body(url)
    
else:
    links(url)

