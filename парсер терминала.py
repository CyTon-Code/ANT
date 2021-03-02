"""
'echo "Hello World!/n"' - Парсер пробелов: parser_probible()
["echo", '"Hello', 'World!/n"']- Парсер кавычек. - разъединяет все
 строки отделяя кавычки отдельно: parser_kavichek
clear()
["echo", '"', "Hello", "World!/n", '"'] - склеивание строк между кавычек
 пробелами:
clear()
["echo", "Hello World!/n"]
clear()


clear - чистка: пустые строки, точки и прочие элементы черного списка.
- parser_clear


реализация:
"""
clear = ["", "."]
def parser_probible(stroka, sep=" "):
    tmp = []
    stroka += sep
    text = ""

    for i in stroka:
        if i == sep:
            tmp.append(text)
            text = ""
        else:
            text += i
    print(stroka, tmp, text, sep)
    return tmp
def parser_kavichek(stroka, sep='"'):
    # if not sep in stroka:
        # return [stroka]
    tmp = []
    # stroka += sep
    text = ""

    for i in stroka:
        if i == sep:
            # if not text in clear:
            tmp.append(text)
            tmp.append(sep)
            text = ""
        else:
            text += i
    # print(stroka, tmp, text, sep)
    # if not text in clear:
    tmp.append(text)
    return tmp
def parser_clear(stroka):
    tmp = []
    for i in stroka:
        if not i in clear:
            tmp.append(i)
    return tmp
def glay_kavichek(rmp, cal='"', sep=" "):
    tmp = []
    text = ""
    flag = False
    blag = None
    # TODO: Нужно както между кавычек строки склеивать пробелами


    for i in rmp:
        if i == cal:
            flag = not flag
            # if flag:
                # i = " "
            # else:
                # i = ""

        text += i
        if flag:
            # text += i
            # if blag:
                # text += sep
            # print(1, flag, blag, text, tmp, rmp, cal)
            pass
        else:
            tmp.append(text.replace('"', ""))
            text = ""
        blag = flag
    # print(1, flag, blag, text, tmp, rmp, cal)

    print(tmp)


stroka = 'echo "Hello World!/n"'
stroka = parser_probible(stroka)
print(stroka)

tmp = []
for i in stroka:
    tmp = tmp + [*parser_kavichek(i)]
    # print(i)
print(tmp)
tmp = parser_clear(tmp)
print(tmp)
glay_kavichek(tmp)
# print(tmp)
