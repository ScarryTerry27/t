from faker import Faker
#
# with open('text.txt', 'w', encoding='utf-8') as file:
#     for _ in range(10):
#         file.write(f"{_} {x.name()}\n")

# 1
with open('text.txt', 'r', encoding='utf-8') as file:
    lst = file.read().split()
    ls = [i for i in lst if len(i) > 6]
    with open('newnew', 'w', encoding='utf-8') as new:
        new.write(' '.join(ls))

# 2
with open('text.txt', 'r', encoding='utf-8') as file_old:
    with open('new_txt2.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(file_old.read())

# 3
with open('text.txt', 'r', encoding='utf-8') as file_old:
    lines = [i.strip() for i in file_old.readlines()][::-1]
    with open('new_txt_3.txt', 'w', encoding='utf-8') as new_file:
        for line in range(len(lines)):
            new_file.write(f"{line} {lines[line][1:]}\n")


# 4
with open('text.txt', 'r', encoding='utf-8') as file_old:
    lines = [i.strip() for i in file_old.readlines()][::-1]
    with open('new_txt_4.txt', 'w', encoding='utf-8') as new_file:
        for line in range(len(lines)):
            if ',' not in lines[line]:
                lines.insert(line, '*'*12)
                break
        else:
            lines.insert(0, '*' * 12)
        new_file.write('\n'.join(lines[::-1]))


# 5
with open('text.txt', 'r', encoding='utf-8') as file_old:
    word = input()
    n = sum([1 for i in file_old.read().split() if i.startswith(word)])
    print(n)


# 6
def ret_sb(s):
    return ['*', '&'][s == '*']


with open('text.txt', 'r', encoding='utf-8') as file_old:
    text = (i if i not in ('*', '&') else ret_sb(i) for i in file_old.read())
    with open('new_txt_5.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(''.join(list(text)))


# 7

x = Faker()

s = [x.name() for i in range(10)]
with open('text_array', 'w', encoding='utf-8') as file:
    file.write('\n'.join(s))

s = [x.name() for i in range(10)]
with open('text_array', 'w', encoding='utf-8') as file:
    file.write('\n'.join(s))