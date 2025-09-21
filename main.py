# main.py

from application.salary import calculate_salary
from application.db.people import get_employees, save_employee
from datetime import datetime


def main():
    # Выводим текущее время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущая дата и время: {current_time}")

    while True:
        print("\nВыберите действие:")
        print("1. Показать список сотрудников")
        print("2. Добавить сотрудника")
        print("3. Вычислить зарплаты сотрудников")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            employees = get_employees()
            if employees:
                print("\nСписок сотрудников:")
                for emp in employees:
                    print(f"{emp['first_name']} {emp['last_name']} ({emp['position']})")
            else:
                print("Сотрудников нет.")

        elif choice == '2':
            first_name = input("Введите имя сотрудника: ")
            last_name = input("Введите фамилию сотрудника: ")
            position = input("Введите должность сотрудника: ")
            base_salary = float(input("Введите почасовую ставку сотрудника: "))
            hours_worked = float(input("Введите количество отработанных часов: "))
            save_employee(first_name, last_name, position, base_salary, hours_worked)
            print("Сотрудник добавлен.")

        elif choice == '3':
            employees = get_employees()
            total_salary = 0
            print("\nСписок сотрудников и их зарплаты:")
            for emp in employees:
                salary = calculate_salary(emp['base_salary'], emp['hours_worked'])
                total_salary += salary

                print(f"{emp['first_name']} {emp['last_name']} ({emp['position']}): {salary} руб.")
            print(f"\nОбщая зарплата сотрудников: {total_salary} руб.")

        elif choice == '4':
            print("Выход из программы.")
            break

    else:
        print("Неверный выбор. Пожалуйста, выберите действие снова.")

if __name__ == "__main__":
    main()
