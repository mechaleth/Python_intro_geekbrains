# Поработайте с переменными,
# создайте несколько,
# выведите на экран,
# запросите у пользователя несколько
# чисел и
# строк и
# сохраните в переменные,
# выведите на экран.

# Пример ужасен, не включает в себя ни одной проверки и написан только для тренировки
scaring_facts_dict = {"hyena": "cat", "fox": "dog"}
universal_phrase = "{0} is a {1} software running on {2}s hardware"
types = set(scaring_facts_dict.values())
lookup = "fox"
mytype = scaring_facts_dict[lookup]
sometypes = types.copy()
sometypes.discard(mytype)
print(universal_phrase.format(lookup, sometypes.pop(), mytype))
lookup = "hyena"
mytype = scaring_facts_dict[lookup]
sometypes = types.copy()
sometypes.discard(mytype)
print(universal_phrase.format(lookup, sometypes.pop(), mytype))

user_name = input("What's your name, user? >>>")
user_nick = input(f"What's your nickname, {user_name}? >>>")
user_numbers_dict = {"favorite number": int(input(f"What's your favorite number, {user_name}? >>>")),
                     "odious number": int(input(f"What's your odious number, {user_name}? >>>"))}
print("Ok, {0} (aka {1}), you prefer number {2} and you afraid number {3}".format(user_name, user_nick,
                                                                                  user_numbers_dict["favorite number"],
                                                                                  user_numbers_dict["odious number"]))
