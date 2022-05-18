# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from collections.abc import Iterable


class Office_Equipment:
    # то нет смысла дополнять, только не изменять
    _placement_types = ("Настольный", "Переносной", "Напольный")
    #  это можно дополнить, но безопасно...
    _interface_types = {"USB", "DVI", "HDMI", "Bluetooth", "Wi-Fi"}

    # производитель
    _manufacturer: str
    # размещение - настольный, переносной, напольный
    _placement: str
    # тип устройства
    _type: str
    # название устройства
    _name: str

    def __init__(self, manufacturer: str, name: str, eq_type: str, placement: str, interfaces: list):
        # интерфейсы, разъёмы
        # если объявить вне конструктора
        # то один лист будет для всех объектов
        # всех унаследованных классов
        self._interfaces = []
        self._manufacturer = manufacturer
        self._name = name
        self._type = eq_type
        self.placement = placement
        self.interfaces = interfaces

    @classmethod
    def get_placement_types(cls) -> tuple:
        return cls._placement_types

    @classmethod
    def get_interface_types(cls) -> list:
        return cls._interface_types.copy()

    @classmethod
    def add_interface_types(cls, value):
        if isinstance(value, list):
            cls._interface_types.update(set(value))
        elif isinstance(value, set):
            cls._interface_types.update(value)
        elif isinstance(value, str):
            cls._interface_types.add(value)
        else:
            raise TypeError("Expected a string")

    @property
    def placement(self):
        return self._placement

    @placement.setter
    def placement(self, value: str):
        if value not in Office_Equipment.get_placement_types():
            message = f'{value} not in {self.__class__.__name__}.get_placement_types()'
            raise ValueError(message)
        self._placement = value

    @property
    def interfaces(self):
        return self._interfaces.copy()

    @interfaces.setter
    def interfaces(self, value):
        if isinstance(value, list) or isinstance(value, set):
            if set(value).issubset(Office_Equipment.get_interface_types()):
                self._interfaces.extend(value)
                return
        elif value in Office_Equipment.get_interface_types():
            self._interfaces.append(value)
            return
        raise ValueError(f"{value} not in {self.__class__.__name__}.get_interface_types()")

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model_type(self):
        return self._type

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'{self._placement} {self.manufacturer} {self.name} {self._type}'

    def __repr__(self):
        return f'{self._placement} {self.manufacturer} {self.name} {self._type}'


class Paper_Equipment(Office_Equipment):
    # возможные форматы листа
    # вообще, их куча
    _available_formats = {"A0", "A1", "A2", "A3", "A4", "A5"}

    def __init__(self, manufacturer: str, name: str, eq_type: str, placement: str,
                 interfaces: list, formats: list):
        # конкретный формат
        self._formats = []
        self.paper_formats = formats
        super().__init__(manufacturer, name, eq_type, placement, interfaces)

    @classmethod
    def get_available_formats(cls):
        return cls._available_formats.copy()

    @property
    def paper_formats(self) -> list:
        return self._formats.copy()

    @paper_formats.setter
    def paper_formats(self, value):
        if isinstance(value, list) or isinstance(value, set):
            if set(value).issubset(Paper_Equipment.get_available_formats()):
                self._formats.extend(value)
        elif value in Paper_Equipment.get_available_formats():
            self._formats.append(value)
        else:
            raise ValueError(f"{value} not in {self.__class__.__name__}.get_available_formats()")


class Printer(Paper_Equipment):
    # Возможные типы печати
    _print_types = ('LED', "laser", "jet", "sublime", "thermo")

    # тип печати принтера
    _print_type: str
    # цветная или ч/б...
    _color_print_schema: bool = False
    # скорость печати
    _print_speed: int

    def _specific_print_sets(self, print_type: str, color_schema: bool, print_speed: int):
        if print_speed >= 0:
            self._print_speed = print_speed
        else:
            raise ValueError("Print speed must be a positive!")
        self.print_type = print_type
        self._color_print_schema = color_schema

    # много аргументов - только именованные аргументы
    def __init__(self, *, manufacturer: str, name: str, placement: str, interfaces: list,
                 formats: list, print_type: str, color_schema: bool, print_speed: int):
        self._specific_print_sets(print_type, color_schema, print_speed)
        super().__init__(manufacturer, name, 'Printer', placement, interfaces, formats)

    @classmethod
    def get_print_types(cls):
        return cls._print_types

    @property
    def print_type(self):
        return self._print_type

    # пока что сеттер задан только для удобства
    # инициализации в __init__
    @print_type.setter
    def print_type(self, value: str):
        assert '_print_type' not in self.__dict__, "Print type already sets"
        if value not in Printer.get_print_types():
            raise ValueError(f"{value} not in {self.__class__.__name__}.get_print_types()")
        self._print_type = value

    @property
    def color_print_schema(self) -> bool:
        return self._color_print_schema

    @property
    def print_speed(self):
        return self._print_speed


class Scanner(Paper_Equipment):
    # возможные типы сканеров
    _scanner_types = ('3D', 'Tablet', 'Pull-through', 'Portable', 'Slide scanner', 'Photoscanner')
    # возможные типы датчиков сканера
    _sensor_types = ('CCS', 'CIS', 'CMOS')
    # тип сканера
    _scanner_type: str
    # тип датчика
    _sensor_type: str
    # цветная или ч/б схема сканирования
    _color_scan_schema: bool
    # скорость сканирования
    _scan_speed: int

    def _specific_scan_sets(self, scanner_type: str, sensor_type: str, color_schema: bool,
                            scan_speed: int):
        if scan_speed >= 0:
            self._scan_speed = scan_speed
        else:
            ValueError("Scan speed must be a positive!")
        self.scanner_type = scanner_type
        self.sensor_type = sensor_type
        self._color_scan_schema = color_schema

    # много аргументов - только именованные аргументы
    def __init__(self, *, manufacturer: str, name: str, placement: str, interfaces: list,
                 formats: list, scanner_type: str, sensor_type: str, color_schema: bool,
                 scan_speed: int):
        self._specific_scan_sets(scanner_type, sensor_type, color_schema, scan_speed)
        super().__init__(manufacturer, name, 'Scanner', placement, interfaces, formats)

    @classmethod
    def get_scanner_types(cls):
        return cls._scanner_types

    @classmethod
    def get_sensor_types(cls):
        return cls._sensor_types

    @property
    def scanner_type(self):
        return self._scanner_type

    # пока что сеттер задан только для удобства
    # инициализации в __init__
    @scanner_type.setter
    def scanner_type(self, value: str):
        assert '_scanner_type' not in self.__dict__, "Print type already sets"
        if value not in Scanner.get_scanner_types():
            raise ValueError(f"{value} not in {self.__class__.__name__}.get_scanner_types()")
        self._scanner_type = value

    @property
    def sensor_type(self):
        return self._sensor_type

    # пока что сеттер задан только для удобства
    # инициализации в __init__
    @sensor_type.setter
    def sensor_type(self, value: str):
        assert '_sensor_type' not in self.__dict__, "Color schema already sets"
        if value not in Scanner.get_sensor_types():
            raise ValueError(f"{value} not in {self.__class__.__name__}.get_sensor_types()")
        self._sensor_type = value

    @property
    def scan_color_schema(self) -> bool:
        return self._color_scan_schema

    @property
    def scan_speed(self):
        return self._scan_speed


class Xerox(Printer, Scanner):
    """Многофункциональное устройство - возможность печати и сканирования"""

    # много аргументов - только именованные аргументы
    def __init__(self, *, manufacturer: str, name: str, placement: str, interfaces: list,
                 formats: list, print_type: str, color_print_schema: bool, print_speed: int,
                 scanner_type: str, sensor_type: str, color_scan_schema: bool,
                 scan_speed: int
                 ):
        self._specific_print_sets(print_type, color_print_schema, print_speed)
        self._specific_scan_sets(scanner_type, sensor_type, color_scan_schema, scan_speed)
        super(Scanner, self).__init__(manufacturer, name, 'PFE', placement, interfaces, formats)
        # а вот так бы не получили конструктор из Paper_Equipment
        # super(Printer, self).__init__(manufacturer, name, 'PFE', placement, interfaces, formats)


if __name__ == '__main__':
    print(f'Интерфейсы {Office_Equipment.get_interface_types()}')
    print(f'Типы принтера {Printer.get_print_types()}')
    print(f'Форматы {Paper_Equipment.get_available_formats()}')
    print(f'Расположение {Paper_Equipment.get_placement_types()}')
    print(f'Типы сканера {Scanner.get_scanner_types()}')
    print(f'Типы сенсора {Xerox.get_sensor_types()}')
    try:
        # Office_Equipment("Canon", "Canon ght900", "TechnoPencil", "Напотолочный", ["USB", "HDMI"])
        # Office_Equipment("Canon", "Canon ght900", "TechnoPencil", "Напольный", ["USB1", "HDMI"])
        # Printer(manufacturer="Xerox", name="Pbpfd", placement="Настольный", interfaces="USB",
        # formats=['A0', 'A1'], print_type="Лапки", color_schema=False, print_speed=-100)
        Scanner(manufacturer="HP", name="Ohho", placement="Переносной", interfaces=["USB", "HDMI"],
                formats=['A0', 'A1'], scanner_type="Глаза", sensor_type="Вкусовые сосочки",
                color_schema=True, scan_speed=10)
    except ValueError as error:
        print(error)
    equipments = (Office_Equipment("Canon", "ght900", "TechnoPencil", "Напольный", ["USB", "HDMI"]),
                  Xerox(manufacturer="HP", name="Ohho", placement="Напольный",
                        interfaces=["USB", "USB", "HDMI", 'DVI', 'USB', 'Wi-Fi', 'Bluetooth'], formats=['A0', 'A1'],
                        print_type=Printer.get_print_types()[1], color_print_schema=True,
                        print_speed=10, scanner_type=Scanner.get_scanner_types()[0],
                        sensor_type=Scanner.get_sensor_types()[2], color_scan_schema=True, scan_speed=10),
                  Printer(manufacturer="Xerox", name="Pbpfd", placement="Настольный", interfaces="USB",
                          formats=['A0', 'A1'], print_type=Printer.get_print_types()[2],
                          color_schema=False, print_speed=100),
                  Scanner(manufacturer="HP", name="Ohho", placement="Переносной", interfaces=["USB", "HDMI"],
                          formats=['A0', 'A1'], scanner_type=Scanner.get_scanner_types()[1],
                          sensor_type=Scanner.get_sensor_types()[2], color_schema=False, scan_speed=10)
                  )

    for equipm in equipments:
        print(equipm.manufacturer)
        print(equipm.name)
        print(equipm.placement)
        print(equipm.model_type)
        print(equipm.interfaces)
        if isinstance(equipm, Paper_Equipment):
            print(equipm.paper_formats)
        if isinstance(equipm, Printer):
            print(equipm.print_speed)
            print(equipm.print_type)
            print(equipm.color_print_schema)
        if isinstance(equipm, Scanner):
            print(equipm.scanner_type)
            print(equipm.sensor_type)
            print(equipm.scan_color_schema)
            print(equipm.scan_speed)
