# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за
# приём оргтехники на склад и передачу в
# определенное подразделение компании.
# Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру,
# например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# как будто всё в одном файле
from task_4_5_6_equipment import *


class NotIsInstance(ValueError):
    def __init__(self, variable, variable_name: str, datatype: type, *args, **kvargs):
        self._message = f'Некорректный тип данных {variable_name} ожидался' \
                        f' {datatype.__name__}, получен {type(variable)}'
        super().__init__(args, kvargs)

    def __str__(self):
        return self._message


class Office_Equipment_Store:
    _max_capacity: int
    # словарь выглядит таким образом
    # {производитель : {(название модели, тип): объекты}}
    _store_equipments: dict

    def __init__(self, max_capacity):
        assert max_capacity >= 0, "Объём склада не может быть отрицательным"
        self._max_capacity = max_capacity
        self._current_count = 0
        self._store_equipments = {}

    def _get_model_type_list(self, manufacturer: str, model: str, model_type: str) -> list:
        manufacturers_dict = \
            self._store_equipments.setdefault(manufacturer, {})
        return manufacturers_dict.setdefault((model, model_type), [])

    @staticmethod
    def __get_maker_model_type(office_equipment: Office_Equipment) -> tuple:
        return office_equipment.manufacturer, office_equipment.name, office_equipment.model_type

    def _append_equipment(self, office_equipment: Office_Equipment):
        """
        Добавление единицы оргтехники в
        необходимые стуктуры хранения склада

        :param office_equipment: офисная техника
        :return: None
        """
        maker_name, model_name, model_type = \
            self.__get_maker_model_type(office_equipment)
        models_type_list = self._get_model_type_list(maker_name, model_name, model_type)
        models_type_list.append(office_equipment)
        self._current_count += 1

    @property
    def common_count(self):
        return self._current_count

    def append_equipment(self, office_equipment):
        """
        Добавляем оргтехнику на склад

        :param office_equipment: единичная оргтехника или итерируемый объект
        :return: None. Может быть выброшено ValueError!
        """
        if self._current_count >= self._max_capacity:
            raise ValueError("Store overloaded!")
        # как правило, интересуют производитель и модель
        # характеристики - это не про склад
        if isinstance(office_equipment, Office_Equipment):
            self._append_equipment(office_equipment)
        elif isinstance(office_equipment, Iterable):
            # Для итерируемых объектов исключений не будет
            # Как будто мы пытаемся разгрузить партию,
            # пришедшую на склад, пусть и не оттуда)
            for unit in office_equipment:
                if self._current_count >= self._max_capacity:
                    break
                if not isinstance(unit, Office_Equipment):
                    continue
                self._append_equipment(unit)
        else:
            message = f"That's not an {Office_Equipment.__name__} object"
            raise ValueError(message)

    def get_equipment(self, manufacturer: str, name: str, count: int) -> list:
        """
        Получить со склада технику по производителю и названию

        :param manufacturer: производитель оргтехники
        :param name: название
        :param count: количество оргтехники
        :return: список из требуемой оргтехники. Или ошибки, если ничего нет.
        """
        # куча проверок, прям как в 6 задании просили
        if not isinstance(manufacturer, str):
            raise NotIsInstance(manufacturer, 'manufacturer', str)
        if not isinstance(name, str):
            raise NotIsInstance(name, 'name', str)
        if not isinstance(count, int):
            raise NotIsInstance(count, 'count', int)
        assert not count < 0, "Если Вы хотите пожертвовать оргтехнику, то это другой метод!"
        assert count != 0, "Не стоит нас напрасно беспокоить!"
        if manufacturer not in self._store_equipments.keys():
            raise ValueError("Такого производителя нет на складе!")
        manufacturer_models_types = self._store_equipments.get(manufacturer)
        if name not in {model for model, _ in manufacturer_models_types.keys()}:
            raise ValueError("Такой модели нет на складе!")
        # models_types = [(model, model_type)
        # мне нужны ключи, причем не уникальные,
        # а все, в количестве объектов данной модели
        # данного производителя на складе
        models_types_tuple = tuple(((model, model_type)
                                    for (model, model_type), model_items in manufacturer_models_types.items()
                                    for _ in model_items
                                    if model == name))
        models_number = len(models_types_tuple)
        if models_number < count:
            # f-строки не всегда корректно выводятся непосредственно из исключения
            message = f"Увы, на складе только {models_number} экземпляров!"
            raise ValueError(message)
        lost_models = []
        for cnt, model_type_pair in enumerate(models_types_tuple, start=0):
            if cnt >= count:
                break
            models_list = manufacturer_models_types.get(model_type_pair)
            lost_models.append(models_list.pop())
            if not bool(models_list):
                # если список пуст, зачем нам словарь?
                manufacturer_models_types.pop(model_type_pair)
            if not bool(manufacturer_models_types):
                # если словарь пуст, зачем нам этот словарь в словаре?
                self._store_equipments.pop(manufacturer)
            self._current_count -= 1

        return lost_models

    def get_models(self, type_: str, manufacturer: str) -> set:
        if not isinstance(manufacturer, str):
            raise NotIsInstance(manufacturer, 'manufacturer', str)
        if not isinstance(type_, str):
            raise NotIsInstance(type_, 'name', str)
        if manufacturer not in self._store_equipments.keys():
            raise ValueError("Такого производителя нет на складе!")
        manufacturer_models_types = self._store_equipments.get(manufacturer)
        if type_ not in (model_type for model, model_type in manufacturer_models_types.keys()):
            raise ValueError("Нет такого типа оргтехники!")
        return {model
                for model, model_type in manufacturer_models_types.keys()
                if model_type == type_}


if __name__ == "__main__":
    # поле для экспериментов))
    # Названия для техники разных типов ожидаются уникальные
    # Не будет принтер и сканер у одного производителя называться одинаково
    # Но мы предусмотрели реакцию)
    equipments = (Office_Equipment("Canon", "Canon ght900", "TechnoPencil", "Напольный", ["USB", "HDMI"]),
                  Xerox(manufacturer="HP", name="Ohho", placement="Напольный",
                        interfaces=["USB", "USB", "HDMI", 'DVI', 'USB', 'Wi-Fi', 'Bluetooth'], formats=['A0', 'A1'],
                        print_type=Printer.get_print_types()[1], color_print_schema=True,
                        print_speed=10, scanner_type=Scanner.get_scanner_types()[0],
                        sensor_type=Scanner.get_sensor_types()[2], color_scan_schema=True, scan_speed=10),
                  Printer(manufacturer="Xerox", name="Pbpfd", placement="Настольный", interfaces="USB",
                          formats=['A0', 'A1'], print_type=Printer.get_print_types()[2],
                          color_schema=False, print_speed=100),
                  Printer(manufacturer="Xerox", name="ghtad", placement="Настольный", interfaces="USB",
                          formats=['A0', 'A1'], print_type=Printer.get_print_types()[2],
                          color_schema=False, print_speed=100),
                  Printer(manufacturer="HP", name="Pbpfd", placement="Настольный", interfaces="USB",
                          formats=['A0', 'A1'], print_type=Printer.get_print_types()[2],
                          color_schema=False, print_speed=100),
                  Printer(manufacturer="HP", name="Pbpfd", placement="Настольный", interfaces="USB",
                          formats=['A0', 'A1'], print_type=Printer.get_print_types()[2],
                          color_schema=False, print_speed=100),
                  Scanner(manufacturer="HP", name="Ohho", placement="Переносной", interfaces=["USB", "HDMI"],
                          formats=['A0', 'A1'], scanner_type=Scanner.get_scanner_types()[1],
                          sensor_type=Scanner.get_sensor_types()[2], color_schema=False, scan_speed=10),
                  Scanner(manufacturer="HP", name="Ohho", placement="Переносной", interfaces=["USB", "HDMI"],
                          formats=['A0', 'A1'], scanner_type=Scanner.get_scanner_types()[1],
                          sensor_type=Scanner.get_sensor_types()[2], color_schema=False, scan_speed=10),
                  Scanner(manufacturer="HP", name="Ohhlo", placement="Переносной", interfaces=["USB", "HDMI"],
                          formats=['A0', 'A1'], scanner_type=Scanner.get_scanner_types()[1],
                          sensor_type=Scanner.get_sensor_types()[2], color_schema=False, scan_speed=11),
                  Scanner(manufacturer="Canon", name="Ohho", placement="Переносной", interfaces=["USB", "HDMI"],
                          formats=['A0', 'A1'], scanner_type=Scanner.get_scanner_types()[1],
                          sensor_type=Scanner.get_sensor_types()[2], color_schema=False, scan_speed=10)
                  )

    current_store = Office_Equipment_Store(18)
    current_store.append_equipment(equipments)
    try:
        for equipment in equipments:
            current_store.append_equipment(equipment)
    except ValueError as value_error:
        print(value_error)
    print(current_store.get_models("Scanner", "HP"))
    print(current_store.get_models("Printer", "HP"))
    try:
        print(current_store.get_models("Printer", "Canon"))
    except ValueError as value_error:
        print(value_error)
    print(f"Equipments count is {current_store.common_count}")
    print(current_store.get_equipment("HP", "Ohho", 3))
    print(f"Equipments count is {current_store.common_count}")
    print(current_store.get_equipment("HP", "Ohho", 2))
    print(f"Equipments count is {current_store.common_count}")
    print(current_store.get_models("Scanner", "HP"))

    try:
        print(current_store.get_models(5, "HP"))
        # print(current_store.get_models("Scanner", 7))
    except NotIsInstance as error:
        print(error)
    try:
        # print(current_store.get_equipment("HP", "Ohho", 0))
        print(current_store.get_equipment("HP", "Ohho", -1))
    except AssertionError as error:
        print(error)
