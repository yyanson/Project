en_ru = {1: ['One', 'Один'], 2: ['Two', 'Два'], 3: ['Three', 'Три'], 4: ['Four', 'Четыре']}  # словарь для перевода
with open(r"C:\Users\yyans\project_Python\task_5-4_ru.txt", "w+") as ru_file:  # создаем файл не в директории скрипта
    with open(r"C:\Users\yyans\project_Python\task_5-4_en.txt", "r") as en_file:  # файл-источник не в папке скрипта
        i = 1  # счетчик
        for line in en_file:
            ru_file.writelines(line.replace(en_ru.get(i)[0], en_ru.get(i)[1]))  # записываем строки, переводя по словарю
            i += 1
