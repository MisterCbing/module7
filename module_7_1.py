f = open('text.txt', 'r', encoding='utf-8')
for s in f:
    print(s.strip())
f.close()