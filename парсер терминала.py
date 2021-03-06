"""
    'echo "Hello World!/n"' - parser пробелов: parser_space()
    parser_clear()
    ["echo", '"Hello', 'World!/n"']- parser кавычек. - разъединяет все
     строки отделяя кавычки отдельно: parser_braces
    parser_clear()
    ["echo", '"', "Hello", "World!/n", '"'] - склеивание строк между кавычек
     пробелами: glue_between_quotes
    parser_clear()
    ["echo", "Hello World!/n"]
    parser_clear()


    clear - чистка: пустые строки, точки и прочие элементы черного списка.
    - parser_clear


реализация:
"""
# TODO: glue_between_quotes -  сепаратором склеиваются только строки
#  между кавычек. кавычки убираю только если между ними 1 слово.

from additional.parser_space import parser_space
from additional.parser_braces import parser_braces
from additional.parser_clear import parser_clear
from additional.glue_between_quotes import glue_between_quotes

string = 'echo "Hello World!/n"'
string = parser_space(string)
print(string)

tmp = []
for i in string:
    tmp = tmp + [*parser_braces(i)]
    # print(i)
print(tmp)
tmp = parser_clear(tmp)
print(tmp)
glue_between_quotes(tmp)
# print(tmp)
