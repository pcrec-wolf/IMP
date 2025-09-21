import pandas as pd
import os

excel_file = 'peoples.xlsx'

def load_employees():
    """Загружает сотрудников из файла Excel."""
    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
        return df.to_dict(orient='records')
    return []

def save_employee(first_name, last_name, position, base_salary, hours_worked):
    """Сохраняет нового сотрудника в файл Excel."""
    employee = {
        'first_name': first_name,
        'last_name': last_name,
        'position': position,
        'base_salary': base_salary,
        'hours_worked': hours_worked
    }

    # Загружаем текущие данные о сотрудниках
    employees = load_employees()

    # Добавляем нового сотрудника
    employees.append(employee)

    # Сохраняем всех сотрудников обратно в Excel
    df = pd.DataFrame(employees)
    df.to_excel(excel_file, index=False)

def get_employees():
    """Возвращает список сотрудников."""
    return load_employees()
