class Matrix:
    def __init__(self, user_list):
        self.row = len(user_list)  # количество строк в матрице
        self.col = len(user_list[0])  # количество колонок в матрице

        dim_el = 0  # переменная для расчета количества знаков в самом длинном числе матрицы
        self.check = True  # переменная для проверки размера строк в данных пользователя
        for row in user_list:  # в каждой строке матрицы пользователя
            if len(row) != self.col:  # если длина строки не совпадает с длиной первой строки
                self.check = False  # флаг проверки меняется
                break
            for i in row:  # для каждого элемента пользователя
                if len(str(i)) > dim_el:  # если длина элемента больше установленной ранее
                    dim_el = len(str(i))  # меняем переменную знаков элементе матрицы
        if self.check:  # если проверка пройдена
            self.m_list = user_list  # принимаем корректные данные
            self.n = dim_el  # устанавливаем значение для форматирования
        else:
            print(f'{user_list} не хватает элементов матрицы!')  # сообщение о некооректных данных пользователя
            self.m_list = []   # обнуляем матрицу

    def __str__(self):
        self.matrix = ''  # переменная для вывода матрицы на печать
        for row in range(self.row):  # для каждой строки матрицы
            self.format_row = ''  # устанавливаем переменную для форматирования строки матрицы
            for i in self.m_list[row]:  # для каждого элемента матрицы
                s = str(i).rjust(self.n, ' ')  # наращиваем элемент матрицы до формата самого большого элемента
                self.format_row += f' {s}'  # собираем наращенные элементы в форматированную строку
            self.matrix += f'{self.format_row}\n'  # собираем отформатированные строки в матрицу
        return self.matrix

    def __add__(self, other):
        add_matrix = [[self.m_list[row][i] + other.m_list[row][i] for i in range(self.col)] for row in range(self.row)]
        return Matrix(add_matrix)


my_matrix_1 = Matrix([[1, 2, 400, 4], [2, 3, 2, 7], [-3, 4, 5, 5]])
my_matrix_2 = Matrix([[1, 2, 2, 1], [2, -20000, 2, -1003], [3, 3, 3, 2]])
print(my_matrix_1)
print(my_matrix_1 + my_matrix_2)
