import json
import pathlib


class Vacancy:
    """
    Класс для работы с вакансиями.

    """
    name: str
    alternate_url: str
    salary_from: int
    salary_to: int
    city: str

    def __init__(self, name, alternate_url, salary_from, salary_to, city):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from if salary_from else 0
        self.salary_to = salary_to if salary_to else 0
        self.city = city if city else 'Город отсутствует'

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        """
        Метод для создания списка объектов класса
        """
        list_vacanc = []

        for vacancy in vacancies:
            temp = cls(
                name=vacancy["name"],
                alternate_url=vacancy["alternate_url"],
                salary_from=vacancy["salary"]["from"] if vacancy["salary"] else 0,
                salary_to=vacancy["salary"]["to"] if vacancy["salary"] else 0,
                city=vacancy["area"]["name"]
            )
            list_vacanc.append(temp)
        return list_vacanc

    def __gt__(self, other):
        """
        Метод для сравнения и сортировки вакансий по зарплате
        """
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        """
        Метод для сравнения и сортировки вакансий по зарплате
        """
        return self.salary_from < other.salary_from

    def __str__(self):
        """
        Метод для отображения результата поиска в удобном формате
        """
        return (
            f'\nДолжность - {self.name}\n'
            f'Сайт - {self.alternate_url}\n'
            f'Зарплата - {self.salary_from}-{self.salary_to}\n'
            f'Город - {self.city}\n'
        )


class JSONSaver:
    """Сохранение информации о вакансиях в файл в формате .json"""
    __path: pathlib

    def __init__(self, path):
        self.__path = path

    def add_vacancy(self, vacanс: list):
        """Добавление вакансии в файл"""
        with open(self.__path, "w", encoding='utf-8') as file:
            json.dump(vacanс, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        pass

    def loads_json(self) -> list[dict]:
        """
        загружает json-файл и преобразует в список словарей
        :param path: Path
        :return: list[dict]
        """
        with open(self.__path, encoding='utf-8') as file:
            return json.load(file)
