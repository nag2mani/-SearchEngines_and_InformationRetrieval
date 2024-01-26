import requests
response = requests.get("https://zorp.one")
html_content = response.text
print(html_content)

texts = []
start_index = html_content.find("<body")
print(start_index)

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

for t in texts:
    print(t)


