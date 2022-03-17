
def cook_book_read():
    cook_book_list = {}
    with open('file.txt', 'r') as file:
        for line in file:
            dish_name = line.strip()
            count = int(file.readline())
            dish_ingr_list = []
            for item in range(count):
                ingreds = {}
                ingr = file.readline().strip()
                ingreds['ingredient_name'], ingreds['quantity'], ingreds['measure'] = ingr.split('|')
                dish_ingr_list.append(ingreds)
            file.readline()
            cook_book_list[dish_name] = dish_ingr_list
    return cook_book_list

cook_book = cook_book_read()
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingreds_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                our_list = dict()
                if ings['ingredient_name'] not in ingreds_list:
                    our_list['measure'] = ings['measure']
                    our_list['quantity'] = int(ings['quantity']) * person_count
                    ingreds_list[ings['ingredient_name']] = our_list
                else:
                    ingreds_list[ings['ingredient_name']]['quantity'] = ingreds_list[ings['ingredient_name']]['quantity'] + \
                                                                     int(ings['quantity']) * person_count

        else:
            print("Такого нет в кулинарной книге!")
    return ingreds_list


menu = get_shop_list_by_dishes(['Запеченный картофель', ',биг мак'], 2)
print(menu)



