# Hometask for lection 7 "Working with files in Python"

Source file was updated with 2 dishes: "Салат весенний" and "Проверка" for task#2
here it is:
```
....

Салат весенний
5
Помидор | 1 | шт
Огурец | 2 | шт
Оливковое масло | 20 | мл
Соевый соус | 20 | мл
Соль | 3 | г

Проверка
3
Соевый соус | 20 | мл
Помидор | 1 | шт
Огурец | 2 | шт
```

## Task 1 Converting recipies.txt to dictionary cook_book

Log for cook_book:
```
{
'Омлет': [
 {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
 {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
 {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
],
'Утка по-пекински': [
 {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
 {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
 {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'}, 
 {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
], 
'Запеченный картофель': [
 {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'}, 
 {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
 {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
], 
'Фахитос': [
 {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
 {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
 {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
 {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
 {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
], 
'Салат весенний': [
 {'ingredient_name': 'Помидор', 'quantity': 1, 'measure': 'шт'},
 {'ingredient_name': 'Огурец', 'quantity': 2, 'measure': 'шт'},
 {'ingredient_name': 'Оливковое масло', 'quantity': 20, 'measure': 'мл'},
 {'ingredient_name': 'Соевый соус', 'quantity': 20, 'measure': 'мл'},
 {'ingredient_name': 'Соль', 'quantity': 3, 'measure': 'г'}
], 
'Проверка': [
 {'ingredient_name': 'Соевый соус', 'quantity': 20, 'measure': 'мл'},
 {'ingredient_name': 'Помидор', 'quantity': 1, 'measure': 'шт'},
 {'ingredient_name': 'Огурец', 'quantity': 2, 'measure': 'шт'}
]
}
```

## Task 2 Converting cook_book to dictionary for shopping
### Note! Ingredients from different dishes can be meet two or more times

Log for **get_shop_list_by_dishes(["Омлет", "Салат весенний", "Проверка"], 5)**:
```
{
 'Яйцо': {'measure': 'шт', 'quantity': 10},
 'Молоко': {'measure': 'мл', 'quantity': 500},
 'Помидор': {'measure': 'шт', 'quantity': 20},
 'Огурец': {'measure': 'шт', 'quantity': 20},
 'Оливковое масло': {'measure': 'мл', 'quantity': 100},
 'Соевый соус': {'measure': 'мл', 'quantity': 200},
 'Соль': {'measure': 'г', 'quantity': 15}
}

```

Log for **get_shop_list_by_dishes(["Омлет", "Проверка"], 2)**:
```
{
 'Яйцо': {'measure': 'шт', 'quantity': 4},
 'Молоко': {'measure': 'мл', 'quantity': 200},
 'Помидор': {'measure': 'шт', 'quantity': 6},
 'Соевый соус': {'measure': 'мл', 'quantity': 40},
 'Огурец': {'measure': 'шт', 'quantity': 4}
}
```
# Warning! The task 1 has a mistake in output cook_book:

## *Задача №1*
*Должен получится следующий словарь*
```
  'Запеченный картофель': [
	...
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
```
There is no need to add comma at the end of line