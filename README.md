# ANT

ANT - Terminal for user interaction (via modules) with files

ANT - это оболочка, которая помогает взаимодействовать с множествами модулей.
Кроме самой оболочки, ANT еще состоит из огромной кучи библиотек. Эту кучу
библиотек разделили на 3 группы и прозвали модулями. Те модули которые
отвечают: "ДА", "НЕТ", "НИЧЕГО", "Ошибка" - получили название ВОПРОСЫ. Модули
которые же могут обрабатывать данные называют ДОПОЛНИТЕЛЬНЫМИ модулями. Эти две
группы модулей взаимосвязанные. Также есть и третья группа модулей, грубо
говоря ради этой группы и был придуман ANT - это плагины. Плагины это
программы, которым для запуска нужно на время встроить внутрь себя в файлового
менеджера. Плагины могут принимать аргументы как программы и возвращать
значения в виде тарелки на верх сервиза по имени bath.

В файловом менеджере существуют команды. Как правило, команды это имена
плагинов и последующие слова это их аргументы. Но и будут такие плагины для
прямой работы с функциями и вопросами в виде команд.

Цель файлового менеджера, не заставить своим удобным интерфейсом печатать вас
вручную, нет-нет, никак нет. По этому файловый менеджер в самом раннем этапе
разработки будет иметь возможность запускать свои команды 3 способами.

1. запуск команды пройдя этап: запуск ANT -> ввод имени команды (вручную или из
пространства авто-ввода:выбор будет находиться внутри объекта ANT)

2. запуск команды пройдя путь: при запуске ANT первым аргументом указать имя
команды последующие же просто останутся аргументами для команды.

3. запуск команды пройдя путь: при запуске ANT запускаются все скрипты из
auto_path_scripts -> каждая строка в скрипте это одна командная строка.

4. использование модуля запуска команды непосредственно через импорт модулей.

Менеджер также будет удобно использовать и как огромную пачку библиотек,
которая облегчит жизнь.

ANT - ПО которое предназначается для быстрой обработки файлов.

ANT построен на различных библиотеках. Также ANT вплотную связан с модулями.

Сам же ANT без модулей ничего не может.

Модули — как правило питон библиотеки(планируются еще С и С++), цель которых
делать одну конкретную задачу.

Модуль плагины — это внешние модули, которые импортируются одновременно только
одним экземпляром во внутрь ant для исполнения.

Модуль вопросы — это внутренние модули, цель которых узнать ответ на конкретный
вопрос, например: файл есть по этой ссылке?

Модуль функции — это дополнительные модули, цель которых делать мелкие, но в то
же время конкретные задачи. Например: отсортировать файл.

Команды — это такие особые имена в скриптах ANT. В большинстве случаев будут
запускаться только плагины, но планируются плагины которые, помогут запускать и
другие.

Folder bd_v1 - файл который если пуст или отсутствует, дает false, в противном случае
true