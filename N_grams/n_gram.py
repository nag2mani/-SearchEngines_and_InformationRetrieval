import sys

def find_n_gram(text):
    n = int(input("Enter the value of n for n-gram :"))
    lst = text.split()
    for i in range(len(lst) - n + 1):
        print(lst[i:i+n])

text = "After the COVID-19 pandemic forced the world to limit face-to-face contact, businesses were urged to escalate their digital transformation efforts. This came with a myriad of hurdles such as a rise in data breaches and privacy concerns, coupled with progressive regulatory and compliance requirements. As if that were enough, customer demands continue to evolve as consumers seek more convenient and personalized services"

find_n_gram(text)
