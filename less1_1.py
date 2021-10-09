# different types
a = 5
print(a, type(a))
b = 2.56
print(b, type(b))
s = "text"
print(s, type(s))
t = True
print(t, type(t))
f = False
print(f, type(f))
ln = [a, b, s, t, f]
print(ln, type(ln))
tpl = (a, b, s, t, f)
print(tpl, type(tpl))
d = {"int": 5, "float": b, "string": "text", "boolean": t}
print(d, type(d))
print()  # разделяем блоки пустой строкой
# input and print
w = input("Ведите слово из 5 букв: ")
print(f'Вы ввели слово "{w}"')
n = input("Сколько в вашем слове букв? Введите это число: ")
print()  # разделяем блоки пустой строкой
print(f'Прикольно! Вы считаете, что ввели слово из {n} букв?')
print(f'Но {n} уже не совсем число, теперь это лишь знак, символ:')
print(n, "- относится к", type(n))
print(w, "-  тоже относится к", type(w))
print()  # разделяем блоки устой строкой
y = input("Хотите, чтобы знак стал числом? ")
print("Легко! Теперь", n, " относится к", type(int(n)))
