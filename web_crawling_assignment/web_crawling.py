import requests

def title(url):
    response = requests.get(url)
    raw_content = response.text
    title_start = raw_content.find("<title>") + len("<title>")
    title_end = raw_content.find("</title>")
    title = raw_content[title_start:title_end]
    print(title)


def body(url):
    response = requests.get(url)
    html_content = response.text

    texts = []
    start_index = html_content.find("<body")

    if start_index != -1:
        start_index = html_content.find(">", start_index) + 1

        while start_index != -1:
            end_index = html_content.find("<", start_index)
 
            if end_index != -1:
                text = html_content[start_index:end_index].strip()
                if text:
                    texts.append(text)
                start_index = html_content.find(">", end_index) + 1
            else:
                break
    
    result = ''
    for i in texts:
        if (i[0] not in ['.', ',','', ' ', '(', ')', '[', ']', '{', '}', '@', "'", '&', '#', '^']):
            if i[0:3] not in ['-->', 'htt']:
                result = result + i + ' '
    print(result)


def links(url):
    response = requests.get(url)
    raw_content = response.text

    body_raw_content = raw_content

    link = []
    while len(body_raw_content) > 1:
        s = body_raw_content.find("http")
        e = body_raw_content[s:].find('"')
        link.append(body_raw_content[s :s + e])
        body_raw_content = body_raw_content[s + e+1:]

    for j in link[:len(link)-7]:
        if (j[0:6] not in ['https%', 'https&']) and (j[0:5] not in ['http%']):
            print(j)


def main():
    url = input("Enter your Url with https :")
    print('-----------------------------------------------------------------------------')
    print("Tittle :")
    title(url)
    print('-----------------------------------------------------------------------------')
    print("Texts :")
    body(url)
    print('-----------------------------------------------------------------------------')
    print("Links :")
    links(url)

main()





