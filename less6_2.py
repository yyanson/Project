class Road:
    weight_kg_sm = 25
    thickness_sm = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asfalt(self):
        return self._length * self._width * Road.weight_kg_sm * Road.thickness_sm / 1000


my_road = Road(20, 5000)
asfalt = my_road.mass_asfalt()
print("%.0f" % asfalt, 'тонн')
