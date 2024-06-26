from data.settings_path import VACANCIES_PATH
from src.class_load_HH import HeadHunterAPI
from src.class_other import JSONSaver, Vacancy
from src.utils import sort_salary, get_vacancies_by_salary


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    while True:
        salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
        salary = []
        for salar in salary_range:
            if salar.isdigit():
                salary.append(salar)
        if len(salary) != 0:
            break

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)

    # Получение списка вакансий
    hh_vacancies_list = hh_api.get_vacancies

    # Сохранение загруженных вакансий в json файл
    json_saver = JSONSaver(VACANCIES_PATH)
    json_saver.add_vacancy(hh_vacancies_list)
    json_list = json_saver.loads_json()

    # Создания списка объектов класса Vacancy
    vacancies = Vacancy.cast_to_object_list(json_list)

    # СОртировака списка вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(salary_range, vacancies)
    vacancies_sort = sort_salary(ranged_vacancies)

    # Вывод первых N вакансий по зарплате
    top_vacancies = vacancies_sort[0:top_n]
    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
