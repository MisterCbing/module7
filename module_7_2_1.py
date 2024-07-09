def custom_write(fn, strings):
    strings_positions = {}
    with open(fn, 'w', encoding = 'utf-8') as f:
        for i in range(len(strings)):
            bs = f.tell()
            f.write(strings[i] + '\n')
            strings_positions[(i + 1, bs)] = strings[i]
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)