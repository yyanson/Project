# Товары и аналитика
list_of_goods = []
name_of_goods = []
price_of_goods = []
number_of_goods = []
mesure_of_goods = []
n = int(input("Укажите, сколько товаров хотите ввести? "))
i = 1
while i <= n:
    user_list = list(input('Введите товар в формате "название, цена, количество, единица измерения": ').split(', '))
    goods_base = (i, {"название:": user_list[0], "цена:": user_list[1], "кол-во:": user_list[2], "ед.:": user_list[3]},)
    print('Карточка товара:', goods_base)
    list_of_goods.append(goods_base)
    print('Список товаров:', list_of_goods)
    name_of_goods.append(user_list[0])
    price_of_goods.append(user_list[1])
    number_of_goods.append(user_list[2])
    mesure_of_goods.append(user_list[3])
    i += 1
table_of_goods = {"название:": list(set(name_of_goods)), "цена:": list(set(price_of_goods)),
                  "кол-во:": list(set(number_of_goods)), "ед:": list(set(mesure_of_goods))}
print('Аналитика товара:')
print(table_of_goods)
print('А лучше так:')
for key, value in table_of_goods.items():
    print(key, value)
