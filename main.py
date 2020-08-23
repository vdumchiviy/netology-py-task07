import os


def convert_txt_to_dict(fname):
    result = dict()
    file_size = 0

    with open(fname, "r") as f:

        file_size = os.path.getsize(fname)
        while f.tell() < file_size:
            ingredients = list()
            name = f.readline().replace("\n", "")
            ingredients_count = f.readline()

            for i in range(int(ingredients_count)):
                ingredient_from_file = f.readline().replace("\n", "").split(" | ")
                ingredients.append({"ingredient_name": ingredient_from_file[0],
                                    "quantity": int(ingredient_from_file[1]),
                                    "measure": ingredient_from_file[2]})
            f.readline()
            result[name] = ingredients

    return result


def main():
    def get_shop_list_by_dishes(dishes, person_count):
        print(dishes)
        result = dict()

        for dish in dishes:
            for ingredient in cook_book[dish]:
                try:
                    result_dict = result[ingredient["ingredient_name"]]
                    result[ingredient["ingredient_name"]] = {
                        "measure": ingredient["measure"],
                        "quantity": ingredient["quantity"] * person_count + result_dict["quantity"]}
                    # print(result_dict)
                except KeyError:
                    result[ingredient["ingredient_name"]] = {
                        "measure": ingredient["measure"],
                        "quantity": ingredient["quantity"] * person_count}

        return result

    print("# Задача №1")
    cook_book = convert_txt_to_dict("recipies.txt")
    print(cook_book)

    print("# Задача №2")
    print(get_shop_list_by_dishes(["Омлет", "Салат весенний", "Проверка"], 5))
    print(get_shop_list_by_dishes(["Омлет", "Проверка"], 2))


main()
