with open('utf-8.txt', 'w', encoding='utf-8') as f:
    f.write('привет')

with open('windows-1251.txt', 'w', encoding='windows-1251') as f:
    f.write('привет')
def append_to_file(filename, encoding, text):
    with open(filename, 'a', encoding=encoding) as f:
        f.write(text)

append_to_file('utf-8.txt', 'utf-8', ' мир')
append_to_file('windows-1251.txt', 'windows-1251', ' мир')


