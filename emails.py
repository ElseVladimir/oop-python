"""
# Данный код фильтрует список емеил адресов по заданному критерию, в данном случае только gmail.com
# + пароли после него и сохраняет в файл result.txt

"""


import re
pattern = r".+@gmail.com;.+"
with open('emails.txt', 'r') as f, open('result.txt', 'w') as gWrite:
    text = f.read()
    res = re.findall(pattern, text)
    for items in res:
        gWrite.write(items+"\n")
