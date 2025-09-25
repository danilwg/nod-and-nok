import csv

library = {
    "Война и мир": {
        "author": "Л. Толстой", 
        "year": 1869, 
        "ratings": [5, 4, 5]
    },
    "Преступление и наказание": {
        "author": "Ф. Достоевский", 
        "year": 1866, 
        "ratings": [5, 5, 4]
    }
}

def menu():
    """Главное меню программы"""
    while True:
        print("\n" + "="*50)
        print("БИБЛИОТЕЧНАЯ СИСТЕМА")
        print("="*50)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу по названию")
        print("4. Удалить книгу")
        print("5. Добавить новую оценку книге")
        print("6. Вывести список книг, выпущенных после определённого года")
        print("7. Показать все книги с рейтингом выше определённого порога")
        print("8. Экспортировать книги в CSV")
        print("9. Импортировать книги из CSV")
        print("0. Выход")

        choice = input("\nВведите номер действия: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            find_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            add_rating()
        elif choice == '6':
            books_after_year()
        elif choice == '7':
            books_above_rating()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            import_from_csv()
        elif choice == '0':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def add_book():
    """Добавить книгу в библиотеку"""
    try:
        title = input("Введите название книги: ").strip()
        if not title:
            print("Название книги не может быть пустым.")
            return
        
        if title in library:
            print("Книга с таким названием уже существует в библиотеке.")
            return

        author = input("Введите автора: ").strip()
        if not author:
            print("Имя автора не может быть пустым.")
            return
        
        year = int(input("Введите год издания: ").strip())
        if year < 0 or year > 2025:  # Проверка на разумный год
            print("Год издания должен быть положительным числом и не больше текущего года.")
            return

        # Запрашиваем начальные оценки
        ratings_input = input("Введите начальные оценки через запятую (или нажмите Enter для пропуска): ").strip()
        if ratings_input:
            try:
                ratings = [int(r.strip()) for r in ratings_input.split(',')]
                # Проверяем, что все оценки в допустимом диапазоне
                for rating in ratings:
                    if rating < 1 or rating > 5:
                        raise ValueError
            except ValueError:
                print("Оценки должны быть числами от 1 до 5. Начальные оценки не добавлены.")
                ratings = []
        else:
            ratings = []

        library[title] = {"author": author, "year": year, "ratings": ratings}
        print(f"Книга '{title}' успешно добавлена в библиотеку!")
        
    except ValueError:
        print("Ошибка: год издания должен быть целым числом.")
    except Exception as e:
        print(f"Произошла ошибка при добавлении книги: {e}")

def show_books():
    """Показать все книги в библиотеке"""
    if not library:
        print("Библиотека пуста.")
        return
    
    print(f"\nВсего книг в библиотеке: {len(library)}")
    print("-" * 80)
    
    for i, (title, data) in enumerate(library.items(), 1):
        ratings = data["ratings"]
        if ratings:
            avg_rating = sum(ratings) / len(ratings)
            ratings_str = f"{avg_rating:.2f} (оценки: {ratings})"
        else:
            ratings_str = "нет оценок"
        
        print(f"{i}. '{title}'")
        print(f"   Автор: {data['author']}")
        print(f"   Год издания: {data['year']}")
        print(f"   Рейтинг: {ratings_str}")
        print()

def find_book():
    """Найти книгу по названию"""
    search_title = input("Введите название книги для поиска: ").strip().lower()
    found_books = []
    
    for title, data in library.items():
        if search_title in title.lower():
            found_books.append((title, data))
    
    if found_books:
        print(f"\nНайдено книг: {len(found_books)}")
        for title, data in found_books:
            ratings = data["ratings"]
            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            print(f"'{title}' - {data['author']} ({data['year']}), рейтинг: {avg_rating:.2f}")
    else:
        print("Книги с таким названием не найдены.")

def delete_book():
    """Удалить книгу из библиотеки"""
    title = input("Введите название книги для удаления: ").strip()
    
    if title in library:
        confirm = input(f"Вы уверены, что хотите удалить книгу '{title}'? (да/нет): ").strip().lower()
        if confirm in ['да', 'yes', 'y', 'д']:
            del library[title]
            print(f"Книга '{title}' успешно удалена.")
        else:
            print("Удаление отменено.")
    else:
        print("Книга с таким названием не найдена.")

def add_rating():
    """Добавить оценку для книги"""
    title = input("Введите название книги: ").strip()
    
    if title not in library:
        print("Книга с таким названием не найдена.")
        return
    
    try:
        rating = int(input("Введите оценку (1-5): ").strip())
        if rating < 1 or rating > 5:
            print("Оценка должна быть от 1 до 5.")
            return
        
        library[title]["ratings"].append(rating)
        print(f"Оценка {rating} добавлена к книге '{title}'.")
        
    except ValueError:
        print("Оценка должна быть целым числом.")

def books_after_year():
    """Показать книги, выпущенные после указанного года"""
    try:
        year = int(input("Введите год: ").strip())
        
        found_books = []
        for title, data in library.items():
            if data["year"] > year:
                found_books.append((title, data))
        
        if found_books:
            print(f"\nКниги, выпущенные после {year} года:")
            for title, data in found_books:
                print(f"'{title}' - {data['author']} ({data['year']})")
        else:
            print(f"Нет книг, выпущенных после {year} года.")
            
    except ValueError:
        print("Год должен быть целым числом.")

def books_above_rating():
    """Показать книги с рейтингом выше указанного порога"""
    try:
        threshold = float(input("Введите порог рейтинга (0-5): ").strip())
        if threshold < 0 or threshold > 5:
            print("Порог рейтинга должен быть от 0 до 5.")
            return
        
        found_books = []
        for title, data in library.items():
            ratings = data["ratings"]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating > threshold:
                    found_books.append((title, data, avg_rating))
        
        if found_books:
            print(f"\nКниги с рейтингом выше {threshold}:")
            for title, data, avg_rating in found_books:
                print(f"'{title}' - {data['author']} ({data['year']}), рейтинг: {avg_rating:.2f}")
        else:
            print(f"Нет книг с рейтингом выше {threshold}.")
            
    except ValueError:
        print("Порог рейтинга должен быть числом.")

def export_to_csv():
    """Экспортировать библиотеку в CSV файл"""
    filename = input("Введите имя файла для экспорта (например: library.csv): ").strip()
    
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["title", "author", "year", "ratings"])
            
            for title, data in library.items():
                ratings_str = ','.join(map(str, data["ratings"]))
                writer.writerow([title, data["author"], data["year"], ratings_str])
        
        print(f"Библиотека успешно экспортирована в файл '{filename}'.")
        
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def import_from_csv():
    """Импортировать библиотеку из CSV файла"""
    filename = input("Введите имя файла для импорта: ").strip()
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            headers = next(reader)  # Пропускаем заголовок
            
            imported_count = 0
            for row_num, row in enumerate(reader, 2):  # Начинаем с 2 строки
                if len(row) != 4:
                    print(f"Пропуск строки {row_num}: неверное количество столбцов")
                    continue
                
                title, author, year_str, ratings_str = row
                
                if not title or not author:
                    print(f"Пропуск строки {row_num}: отсутствует название или автор")
                    continue
                
                try:
                    year = int(year_str)
                    ratings = [int(r) for r in ratings_str.split(',')] if ratings_str else []
                    
                    # Проверяем оценки на допустимость
                    for rating in ratings:
                        if rating < 1 or rating > 5:
                            raise ValueError(f"Недопустимая оценка: {rating}")
                    
                    library[title] = {"author": author, "year": year, "ratings": ratings}
                    imported_count += 1
                    
                except ValueError as e:
                    print(f"Пропуск строки {row_num}: ошибка в данных - {e}")
        
        print(f"Успешно импортировано {imported_count} книг из файла '{filename}'.")
        
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")

if __name__ == "__main__":
    menu()