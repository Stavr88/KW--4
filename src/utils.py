from src.class_other import Vacancy


def sort_salary(list_vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует список экземпляров класса Vacancy по атрибуту salary
    """
    return sorted(list_vacancies)


def get_vacancies_by_salary(salary_range: str, list_vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Возвращает список экземпляров класса Vacancy по заданным диапазонам зарплаты (атрибут salary)
    """
    salary_range1, salary_range2 = [int(salary.strip()) for salary in salary_range.split('-')]
    list_vacancies_by_salary = []
    for vacancy in list_vacancies:
        if salary_range1 <= vacancy.salary_from <= salary_range2:
            list_vacancies_by_salary.append(vacancy)
    return list_vacancies_by_salary

