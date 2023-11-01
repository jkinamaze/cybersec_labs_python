from math import sqrt


# def encryption(text):
#     cypher_text = ''
#     text = text.upper()
#     for i in range(len(text)):
#         for j in range(len(key)):
#             if text[i] == key[j]:
#                 cypher_text += alphabet[j]
#     print(cypher_text)
#     return cypher_text
# def decryption(cypher_text):
#     text = ''
#     for i in range(len(cypher_text)):
#         for j in range(len(alphabet)):
#             if cypher_text[i] == alphabet[j]:
#                 text += key[j]
#     print(text)


def delete(cypher_text, alph):
    cypher_text = cypher_text.upper()
    new_text = ''
    for i in range(len(cypher_text)):
        for j in range(len(alph)):
            if (cypher_text[i] == alph[j]) or (cypher_text[i] == 'Ё'):
                new_text += alph[j]
                break
    return new_text


def marking_1(cypher_text):
    cypher_text = delete(cypher_text, alphabet)
    dictionary = {}
    for i in range(len(alphabet)):
        count = 0
        for j in range(len(cypher_text)):
            if alphabet[i] == cypher_text[j] or cypher_text[j] == 'Ё':
                count += 1
        dictionary[alphabet[i]] = round(count / len(cypher_text), 5)
    sort_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    x2 = 0
    n = len(alphabet)
    print("Значковая маркировка заданного текста:")
    for i in range(len(sort_data)):
        print(sort_data[i][0], '-', sort_data[i][1])
    for i in range(len(sort_data)):
        x2 += round(((sort_data[i][1] - (n * statistic_1[sort_data[i][0]])) ** 2) / (n * statistic_1[sort_data[i][0]]),
                    5)
    x2 = round(x2, 5)
    print("Хи-квадрат:", x2)
    big_n = sqrt(2 * x2) - sqrt((2 * n) - 1)
    print("Значение статистики:", big_n)
    return sort_data


def marking_2(cypher_text, stat):
    cypher_text = delete(cypher_text, betalpha)
    dictionary = {}
    for j in range(len(betalpha)):
        for k in range(len(betalpha)):
            bi = betalpha[j] + betalpha[k]
            count = 0
            for i in range(len(cypher_text) - 1):
                if (cypher_text[i] + cypher_text[i + 1]) == bi:
                    count += 1
            dictionary[bi] = round(count / len(cypher_text), 5)
    sort_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    x2 = 0
    n = len(alphabet)
    print("Биграмная маркировка заданного текста:")
    for i in range(50):
        print(sort_data[i][0], '-', sort_data[i][1])
    for i in range(len(sort_data)):
        if stat[sort_data[i][0]] == 0:
            x2 += 0
        else:
            x2 += round(((sort_data[i][1] - (n * stat[sort_data[i][0]])) ** 2) / (n * stat[sort_data[i][0]]), 5)
    x2 = round(x2, 5)
    print("Хи-квадрат:", x2)
    big_n = sqrt(2 * x2) - sqrt((2 * n) - 1)
    print("Значение статистики:", big_n)
    return sort_data


def trigrams(cypher_text):
    cypher_text = delete(cypher_text, alphabet)
    for n in range(3, 11):
        dictionary = {}
        for i in range(len(cypher_text) - (n - 1)):
            gram = cypher_text[i:(i + n)]
            br = 0
            for j in range(len(gram)):
                if gram[j] == ' ':
                    br = 1
            if br == 1:
                continue
            count = 0
            for j in dictionary:
                if gram == j:
                    count += 1
                    dictionary[j] += count
                    break
            if count == 0:
                dictionary[gram] = 1
        for word in dictionary:
            dictionary[word] = round(dictionary[word] / len(cypher_text), 5)
        sort_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        print(f'\n{n}-граммы текста:')
        if len(sort_data) >= 50:
            for i in range(50):
                print(sort_data[i][0], '-', sort_data[i][1])
        else:
            for i in range(len(sort_data)):
                print(sort_data[i][0], '-', sort_data[i][1])


alphabet = ' АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
betalpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
with open('lab1_files/text.txt', encoding="utf-8") as file:
    text = file.read()
print(text)
statistic_1 = {}
with open('lab1_files/statistic.txt') as file:
    for line in file:
        statistic_1[line[0]] = float(line[4:len(line) - 1])
print("Значковая маркировка на основе большого текста:")
for a in statistic_1:
    print(a, '-', statistic_1[a])
print("\n")
stat_new = marking_1(text)
statistic_2 = {}
with open('lab1_files/file2.txt') as file:
    for line in file:
        statistic_2[line[:2]] = float(line[4:len(line) - 1])
print("\nБиграмная маркировка на основе большого текста:")
co = 0
for a in statistic_2:
    co += 1
    if co < 50:
        print(a, '-', statistic_2[a])
print("\n")
stat_new_2 = marking_2(text, statistic_2)
trigrams(text)
