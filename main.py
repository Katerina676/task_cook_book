from pprint import pprint

def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            cook_name = line.strip()
            ingredients = int(file.readline().strip())
            ing_list = list()
            for ing in range(ingredients):
                data = file.readline().strip()
                ing_list.append(data)
            file.readline()
            cook_book[cook_name] = []
            for i in ing_list:
                word = i.split('|')
                ingredient_name = word[0]
                quantity = int(word[1])
                measure = word[2]
                cook_book[cook_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    dish_dict = {}
    for dish in dishes:
        for i in cook_book[dish]:
            name = i['ingredient_name']
            measure = i['measure']
            quantity = i['quantity']
            dish_dict[name] = {'measure' : measure, 'quantity' : quantity * person_count}
    return dish_dict

pprint(create_cook_book("receipts.txt"))
pprint(get_shop_list_by_dishes(create_cook_book("receipts.txt"), ['Запеченный картофель', 'Омлет'], 2))
