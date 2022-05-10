# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина`*`ширина`*`масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см`*`число см толщины полотна.
# Проверить работу метода.
#
# 		**Например:** 20м`*`5000м`*`25кг`*`5см = 12500 т

class Road:
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length if length > 0.0 else 0.0
        self._width = width if width > 0.0 else 0.0

    def get_asphalt_mass(self, thickness: float = 5.0, mass_per_sm_sq_m: float = 25.0):
        """
        Расчета массы асфальта, необходимого для покрытия всего дорожного полотна

        :param thickness: толщина полотна, см
        :param mass_per_sm_sq_m: масса асфальта для покрытия одного кв метра
        дороги асфальтом, толщиной в 1 см, кг/м**2*см
        :return: массы асфальта, необходимого для покрытия всего дорожного полотна, кг
        """
        return self._length * self._width * thickness * mass_per_sm_sq_m


if __name__ == "__main__":
    universe_result_str = "Требуемая масса асфальта для толщины {thick} см и " \
                          "массы {mass_per_vol} кг/м**2*см равна {mass} кг"
    current_road = Road(length=float(input("Длина дороги >>>")),
                        width=float(input("Ширина дороги >>>")))
    thickness = float(input("Толщина дороги >>>"))
    # масса асфальта для покрытия одного кв метра +- стандартизирована
    print(universe_result_str.format(thick=thickness,
                                     mass_per_vol=25,
                                     mass=current_road.get_asphalt_mass(thickness)))
    thickness = float(input("Толщина дороги >>>"))
    mass_per_volume = float(input("Масса асфальта для покрытия одного кв метра "
                                  "дороги асфальтом, толщиной в 1 см >>>"))
    print(universe_result_str.format(thick=thickness,
                                     mass_per_vol=mass_per_volume,
                                     mass=current_road.get_asphalt_mass(thickness)))