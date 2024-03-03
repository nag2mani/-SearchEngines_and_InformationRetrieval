import re, requests


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
                if text: #text.isalnum()
                    texts.append(text)
                start_index = html_content.find(">", end_index) + 1
            else:
                break
    # This will remove the unwanted things from the texts and add to the result.
    result = ''
    for i in texts:
        if (i[0] not in ['.', ',','', ' ', '(', ')', '[', ']', '{', '}', '@', "'", '&', '#', '^']):
            if i[0:3] not in ['-->', 'htt', 'jQu']:
                # if i.isalnum():
                    result = result + i + ' '
            
    return result



def tokenize_text(x):
    # It will check first end and last end of words.
    words = re.findall(r'\b\w+\b', x.lower())
    return words


x = body("https://en.wikipedia.org/wiki/Machine_learning")
x = tokenize_text(x)

print(x)