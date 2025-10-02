from functools import reduce

# Исходное меню
menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

current_order = {}

def show_main_menu():
    print("\n" + "=" * 50)
    print("СИСТЕМА УПРАВЛЕНИЯ МЕНЮ КАФЕ")
    print("=" * 50)
    print("1. Просмотр меню")
    print("2. Управление меню")
    print("3. Сформировать заказ")
    print("4. Просмотреть текущий заказ")
    print("5. Выход")
    return input("Выберите действие (1-5): ").strip()

def show_menu_management():
    print("\n" + "-" * 30)
    print("УПРАВЛЕНИЕ МЕНЮ")
    print("-" * 30)
    print("1. Показать отсортированное меню")
    print("2. Посчитать среднюю цену")
    print("3. Добавить/обновить блюда")
    print("4. Удалить блюдо")
    print("5. Показать блюда дешевле цены")
    print("6. Найти самое дешевое/дорогое блюдо")
    print("7. Показать напитки по цене")
    print("8. Назад в главное меню")
    return input("Выберите действие (1-8): ").strip()

# 2. Вывести меню, отсортированное по названию и по цене
def show_sorted_menu():
    print("\nМеню отсортированное по названию:")
    sorted_by_name = sorted(menu.items(), key=lambda x: x[0])
    for item, price in sorted_by_name:
        print(f"  {item}: {price} руб.")
    
    print("\nМеню отсортированное по цене:")
    sorted_by_price = sorted(menu.items(), key=lambda x: x[1])
    for item, price in sorted_by_price:
        print(f"  {item}: {price} руб.")

# 3. Посчитать среднюю цену блюда
def calculate_average_price():
    prices = list(map(lambda x: x[1], menu.items()))
    average = sum(prices) / len(prices) if prices else 0
    print(f"\nСредняя цена блюда: {average:.2f} руб.")
    return average

# 4. Добавить новые блюда в меню
def add_or_update_dishes():
    user_input = input("\nВведите блюда и цены в формате 'блюдо:цена, блюдо:цена': ")
    pairs = list(map(lambda x: x.strip(), user_input.split(',')))
    
    new_items = {}
    for pair in pairs:
        if ':' in pair:
            dish, price = map(lambda x: x.strip(), pair.split(':'))
            if dish and price.isdigit():
                new_items[dish] = int(price)
    
    menu.update(new_items)
    print("Меню обновлено!")
    return new_items

# 5. Удалить блюдо из меню
def remove_dish():
    dish_to_remove = input("\nВведите название блюда для удаления: ").strip().lower()
    if dish_to_remove in menu:
        menu.pop(dish_to_remove)
        print(f"Блюдо '{dish_to_remove}' удалено из меню")
        return True
    else:
        print("Блюдо не найдено в меню!")
        return False

# 6. Показать блюда дешевле определенной цены
def show_dishes_cheaper_than():
    try:
        max_price = int(input("\nВведите максимальную цену: "))
        cheap_dishes = dict(filter(lambda x: x[1] < max_price, menu.items()))
        print(f"Блюда дешевле {max_price} руб.:")
        for dish, price in cheap_dishes.items():
            print(f"  {dish}: {price} руб.")
        return cheap_dishes
    except ValueError:
        print("Ошибка: введите целое число")
        return {}

# 7. Найти самое дешевое и дорогое блюдо
def find_extreme_prices():
    if menu:
        cheapest = min(menu.items(), key=lambda x: x[1])
        most_expensive = max(menu.items(), key=lambda x: x[1])
        print(f"\nСамое дешевое блюдо: {cheapest[0]} - {cheapest[1]} руб.")
        print(f"Самое дорогое блюдо: {most_expensive[0]} - {most_expensive[1]} руб.")
        return cheapest, most_expensive
    else:
        print("Меню пустое!")
        return None, None

# 8. Сделать список только напитков и отсортировать по цене
def get_sorted_drinks():
    drinks = ['coffee', 'tea', 'juice']
    drink_items = list(filter(lambda x: x[0] in drinks, menu.items()))
    sorted_drinks = sorted(drink_items, key=lambda x: x[1])
    print("\nНапитки отсортированные по цене:")
    for drink, price in sorted_drinks:
        print(f"  {drink}: {price} руб.")
    return sorted_drinks

# 9. Сформировать заказ
def create_order():
    global current_order
    print("\nДоступные блюда:")
    for dish, price in menu.items():
        print(f"  {dish}: {price} руб.")
    
    user_input = input("\nВведите список блюд через запятую: ")
    
    # a. Убрать пробелы и привести к нижнему регистру
    dishes = list(map(lambda x: x.strip().lower(), user_input.split(',')))
    
    # b. Проверить, есть ли блюда в меню
    valid_dishes = list(filter(lambda x: x in menu, dishes))
    
    # c. Составить словарь заказа
    current_order = dict(map(lambda dish: (dish, menu[dish]), valid_dishes))
    
    # Проверить невалидные блюда
    invalid_dishes = list(filter(lambda x: x not in menu and x != '', dishes))
    if invalid_dishes:
        print(f"Следующие блюда не найдены в меню: {', '.join(invalid_dishes)}")
    
    if current_order:
        print("Заказ сформирован!")
        show_current_order()
    else:
        print("Заказ не сформирован (нет валидных блюд)")
    
    return current_order

# 10. Посчитать общую стоимость заказа
def calculate_total(order):
    if not order:
        return 0
    
    total = reduce(lambda x, y: x + y, order.values())
    return total

# 11. Показать заказ в красивом виде
def show_order_pretty(order):
    if not order:
        print("Заказ пустой")
        return
    
    print("\nВаш заказ:")
    # Используем enumerate + lambda для красивого вывода
    list(map(lambda item: print(f"  {item[0] + 1}. {item[1][0].title()} – {item[1][1]} руб."), 
             enumerate(order.items())))
    
    total = calculate_total(order)
    print(f"Итого: {total} руб.")
    
    # Проверка заказа
    check_order(order, total)

# 12. Проверить заказ
def check_order(order, total):
    # a. Если сумма больше 500
    if total > 500:
        print("Поздравляем, у вас скидка 10%!")
        discounted_total = total * 0.9
        print(f"Сумма со скидкой: {discounted_total:.2f} руб.")
    
    # b. Если заказ пустой
    elif not any(order.values()) or not order:
        print("Вы ничего не выбрали")

def show_current_order():
    if current_order:
        print("\nТекущий заказ:")
        show_order_pretty(current_order)
    else:
        print("\nТекущий заказ пуст")

def show_simple_menu():
    print("\nТекущее меню:")
    for dish, price in menu.items():
        print(f"  {dish}: {price} руб.")

# Главная функция
def main():
    while True:
        choice = show_main_menu()
        
        if choice == '1':
            show_simple_menu()
        
        elif choice == '2':
            while True:
                sub_choice = show_menu_management()
                
                if sub_choice == '1':
                    show_sorted_menu()
                elif sub_choice == '2':
                    calculate_average_price()
                elif sub_choice == '3':
                    add_or_update_dishes()
                elif sub_choice == '4':
                    remove_dish()
                elif sub_choice == '5':
                    show_dishes_cheaper_than()
                elif sub_choice == '6':
                    find_extreme_prices()
                elif sub_choice == '7':
                    get_sorted_drinks()
                elif sub_choice == '8':
                    break
                else:
                    print("Неверный выбор! Попробуйте снова.")
        
        elif choice == '3':
            create_order()
        
        elif choice == '4':
            show_current_order()
        
        elif choice == '5':
            print("Спасибо за использование системы! До свидания!")
            break
        
        else:
            print("Неверный выбор! Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()