from data.settings_path import VACANCIES_PATH
from src.class_load_HH import HeadHunterAPI
from src.class_other import JSONSaver, Vacancy
from src.utils import sort_salary, get_vacancies_by_salary

# Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)



# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver(vacancy)
# json_saver.add_vacancy()
# json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # while True:
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
        # if salary_range

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)
    hh_vacancies_list = hh_api.vacancies
    json_saver = JSONSaver(VACANCIES_PATH)
    json_saver.add_vacancy(hh_vacancies_list)
    json_list = json_saver.loads_json()
    vacancies = Vacancy.cast_to_object_list(json_list)
    ranged_vacancies = get_vacancies_by_salary(salary_range, vacancies)
    vacancies_sort = sort_salary(ranged_vacancies)
    top_vacancies = vacancies_sort[0:top_n]
    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()






    # ranged_vacancies = get_vacancies_by_salary(salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)



