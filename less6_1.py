import time


class TrafficLight:
    __color__ = ['red', 'yellow', 'green']

    def running(self, start_color, times_ryg, n):
        # определяем стартовый индекс для конкретного светофора:
        start_index = TrafficLight.__color__.index(start_color)
        # формируем цветовой режим для светофора:
        color_mode = sum((TrafficLight.__color__[start_index:], TrafficLight.__color__[:start_index]), [])  #
        # формируем временной режим для светофора:
        times_mode = sum((times_ryg[start_index:], times_ryg[:start_index]), [])
        # выводим режим на дисплей:
        print(color_mode, times_mode)
        # включаем светофор:
        for i in range(n):
            for el in color_mode:
                # переключение цвета на светофоре:
                print(el)
                # заданное время горит текущий цвет:
                time.sleep(times_mode[color_mode.index(el)])


# проверяем цветовой режим светофоров:
if TrafficLight.__color__ != ['red', 'yellow', 'green']:
    print('Неверный цветовой режим!')
else:
    # создаем светофор №1:
    trafficLight_1 = TrafficLight()
    # задаем: начальный цвет, временной режим, количество циклов и вкючаем светофор №1:
    trafficLight_1.running('red', [7, 2, 9], 3)

    # создаем светофор №2:
    trafficLight_2 = TrafficLight()
    # задаем начальный цвет, временной режим, количество циклов и вкючаем светофор #2:
    trafficLight_2.running('yellow', [7, 2, 5], 3)
