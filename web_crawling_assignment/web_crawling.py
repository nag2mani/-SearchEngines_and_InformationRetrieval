import requests

def title(url):
    # This function will print the title of the webpage.

    response = requests.get(url)
    #This raw_content will code all the texts with script from webpages.
    raw_content = response.text
    title_start = raw_content.find("<title>") + len("<title>")
    title_end = raw_content.find("</title>")
    title = raw_content[title_start:title_end]
    print(title)



def body(url):
    # This function will print the content of the body.

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
    # This will remove the unwanted things from the texts and add to the result.
    result = ''
    for i in texts:
        if (i[0] not in ['.', ',','', ' ', '(', ')', '[', ']', '{', '}', '@', "'", '&', '#', '^']):
            if i[0:3] not in ['-->', 'htt', 'jQu']:
                result = result + i + ' '
    print(result)




def links(url):
    # This function will print the links in the webpage.
    response = requests.get(url)
    raw_content = response.text

    body_raw_content = raw_content

    link = []
    while len(body_raw_content) > 1:
        s = body_raw_content.find("https://")
        e = body_raw_content[s:].find('"')
        link.append(body_raw_content[s :s + e])
        body_raw_content = body_raw_content[s + e+1:]
    
    for i in link:
        print(i)




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





