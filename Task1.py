# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def analyze_items(friends_items):
   
    friends = list(friends_items.keys())

    
    items_sets = [set(items) for items in friends_items.values()]

    
    common_items = set.intersection(*items_sets)

  
    unique_items = set.union(*items_sets) - common_items

    
    items_except_one = set()
    friend_without_item = ""
    for friend_index, items_set in enumerate(items_sets):
        other_items_sets = items_sets[:friend_index] + items_sets[friend_index + 1:]
        items_except_current = set.intersection(*other_items_sets)
        items_except_one.update(items_except_current - items_set)
        if not items_except_current - items_set:
            friend_without_item = friends[friend_index]

    return common_items, unique_items, items_except_one, friend_without_item


friends_items = {
    "Друг 1": ("Палатка", "Спальник", "Фонарик", "Котелок"),
    "Друг 2": ("Палатка", "Коврик", "Котелок"),
    "Друг 3": ("Палатка", "Фонарик", "Спички", "Спальник"),
}


common_items, unique_items, items_except_one, friend_without_item = analyze_items(friends_items)


print("Вещи, взятые всеми друзьями:", common_items)
print("Уникальные вещи, есть только у одного друга:", unique_items)
print("Вещи, присутствующие у всех, кроме одного друга:", items_except_one)
print("Друг, у которого отсутствуют данные вещи:", friend_without_item)